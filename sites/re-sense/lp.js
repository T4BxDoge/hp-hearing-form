/* サービス紹介ページ（リジェコミュニティ・DFS Collective）と規約ページの共通の動き。
   会社情報・決済リンクは site.js の SITE にまとめています */

const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

/* ---------- スクロールで現れる演出 ---------- */
(function reveal() {
  const items = [...document.querySelectorAll(".reveal")];
  if (reduceMotion || !("IntersectionObserver" in window)) {
    items.forEach(el => el.classList.add("is-in"));
    return;
  }
  items.forEach(el => {
    const sibs = [...el.parentElement.children].filter(c => c.classList.contains("reveal"));
    el.style.setProperty("--d", (sibs.indexOf(el) * 0.09) + "s");
  });
  const io = new IntersectionObserver(entries => {
    entries.forEach(e => {
      if (e.isIntersecting) { e.target.classList.add("is-in"); io.unobserve(e.target); }
    });
  }, { rootMargin: "0px 0px -8% 0px", threshold: 0.12 });
  items.forEach(el => {
    // 最初から画面内にあるものは隠さない（読めない時間を作らない）
    if (el.getBoundingClientRect().top < window.innerHeight) el.classList.add("is-in");
    else { el.classList.add("pre"); io.observe(el); }
  });
})();

/* ---------- ヘッダーの影・追従ボタン ---------- */
(function scrollUi() {
  const hd = document.querySelector(".lp-hd");
  const fl = document.querySelector(".float-join");
  const plan = document.getElementById("join");
  let ticking = false;
  function update() {
    const y = window.scrollY;
    if (hd) hd.classList.toggle("is-scrolled", y > 8);
    if (fl && plan) {
      const r = plan.getBoundingClientRect();
      const nearPlan = r.top < window.innerHeight && r.bottom > 0;
      fl.classList.toggle("is-show", y > 500 && !nearPlan);
    }
    ticking = false;
  }
  window.addEventListener("scroll", () => { if (!ticking) { requestAnimationFrame(update); ticking = true; } }, { passive: true });
  update();
})();

/* ---------- 紹介リンク（?ref=紹介コード） ----------
   紹介リンクから来たら紹介コードを30日間覚えておき、Stripe の料金表に client-reference-id として渡す。
   申し込むと Stripe の決済に紹介コードが付き、Discord bot が紹介として記録する */
function applyReferral(table) {
  const KEY = "reje_ref", DAYS = 30, valid = c => /^[A-Za-z0-9]{4,20}$/.test(c || "");
  let code = new URLSearchParams(location.search).get("ref");
  try {
    if (valid(code)) {
      localStorage.setItem(KEY, JSON.stringify({ code, at: Date.now() }));
    } else {
      const saved = JSON.parse(localStorage.getItem(KEY) || "null");
      code = saved && Date.now() - saved.at < DAYS * 864e5 ? saved.code : "";
    }
  } catch (e) { if (!valid(code)) code = ""; }
  if (!valid(code)) return;
  const old = table.querySelector("stripe-pricing-table");
  if (!old) return;
  // 料金表が表示されたあとでは属性の変更が効かないことがあるため、属性を付けた新しい料金表に差し替える
  const fresh = document.createElement("stripe-pricing-table");
  for (const a of old.attributes) fresh.setAttribute(a.name, a.value);
  fresh.setAttribute("client-reference-id", code.toUpperCase());
  old.replaceWith(fresh);
}

/* ---------- 入会ボタン（Stripe の決済ページへ） ----------
   SITE.stripe に Payment Link の URL があればそこへ移動。
   空のときは「準備中」と表示して、LINEでの問い合わせに案内する */
(function join() {
  const box = document.getElementById("join");
  if (!box) return;
  const btn = box.querySelector(".join-btn");
  // Stripe の料金表を使うページ（リジェ）：同意のチェックで料金表を表示する
  const table = document.getElementById("ptable");
  if (table) {
<<<<<<< HEAD
=======
    applyReferral(table);
>>>>>>> origin/main
    const ag = box.querySelector(".agree input"), m = box.querySelector(".join-msg");
    const sync = () => {
      table.hidden = !ag.checked;
      m.textContent = ag.checked ? "プランを選んで、お申し込み（決済サービス Stripe）へお進みください" : "上の「同意する」にチェックを入れると、お申し込みの画面が表示されます";
    };
    ag.addEventListener("change", sync); sync();
  }
  if (!btn) return;
  const label = btn.querySelector(".join-label");
  const agree = box.querySelector(".agree input");
  const msg = box.querySelector(".join-msg");
  const plans = [...box.querySelectorAll("[data-plan]")];
  let current = (plans.find(p => p.getAttribute("aria-checked") === "true") || plans[0] || btn).dataset.plan || btn.dataset.plan;

  function render() {
    const p = plans.find(x => x.dataset.plan === current);
    const url = (SITE.stripe || {})[current] || "";
    plans.forEach(x => x.setAttribute("aria-checked", String(x === p)));
    const name = p ? p.dataset.planName : btn.dataset.planName;
    if (url) {
      label.textContent = name ? name + "で入会する" : btn.dataset.default;
      btn.classList.toggle("is-locked", !agree.checked);
      btn.setAttribute("aria-disabled", String(!agree.checked));
      msg.textContent = agree.checked ? "決済ページ（Stripe）に移動します" : "上の「同意する」にチェックを入れてください";
    } else {
      label.textContent = "お申し込み準備中";
      btn.classList.add("is-locked");
      btn.setAttribute("aria-disabled", "true");
      msg.textContent = "現在お申し込みの準備中です。ご興味のある方はLINEからお問い合わせください。";
    }
    btn.href = url || "#join";
  }
  plans.forEach(p => {
    p.addEventListener("click", () => { current = p.dataset.plan; render(); });
    p.addEventListener("keydown", e => {
      if (e.key === " " || e.key === "Enter") { e.preventDefault(); current = p.dataset.plan; render(); }
      if (e.key === "ArrowRight" || e.key === "ArrowLeft" || e.key === "ArrowDown" || e.key === "ArrowUp") {
        e.preventDefault();
        const i = plans.indexOf(p), n = plans[(i + (e.key === "ArrowRight" || e.key === "ArrowDown" ? 1 : plans.length - 1)) % plans.length];
        current = n.dataset.plan; render(); n.focus();
      }
    });
  });
  agree.addEventListener("change", render);
  btn.addEventListener("click", e => {
    if (btn.getAttribute("aria-disabled") === "true") {
      e.preventDefault();
      msg.classList.remove("is-shake"); void msg.offsetWidth; msg.classList.add("is-shake");
      if ((SITE.stripe || {})[current] && !agree.checked) agree.focus();
    }
  });
  render();
})();

/* ---------- 光の線（canvasに画面の解像度で毎フレーム描くので、高解像度でもくっきり） ---------- */
(function glow() {
  const cv = document.querySelector("[data-glow]");
  if (!cv || !cv.getContext) return;
  const ctx = cv.getContext("2d");
  const colors = cv.dataset.glow.split(",");   // 例："#5dff3a,#e4ff3a"
  let W = 0, H = 0, dpr = 1, running = true;
  const start = performance.now();
  function resize() {
    const r = cv.getBoundingClientRect();
    dpr = Math.min(window.devicePixelRatio || 1, 3);
    W = r.width; H = r.height;
    cv.width = Math.round(W * dpr); cv.height = Math.round(H * dpr);
  }
  // 画面を横切るゆるい曲線を数本、ゆっくり波打たせる
  const lines = [
    { y: .62, amp: .10, f: 1.2, sp: .35, w: 2.2, c: 0, a: .9 },
    { y: .70, amp: .08, f: 1.6, sp: -.28, w: 1.2, c: 1, a: .6 },
    { y: .54, amp: .12, f: .9, sp: .22, w: 1, c: 0, a: .45 },
    { y: .80, amp: .06, f: 2.1, sp: .4, w: .8, c: 1, a: .4 }
  ];
  function draw(now) {
    const t = reduceMotion ? 0 : (now - start) / 1000;
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    ctx.clearRect(0, 0, W, H);
    ctx.globalCompositeOperation = "lighter";
    lines.forEach((l, i) => {
      const intro = reduceMotion ? 1 : Math.min(1, Math.max(0, (t - i * .15) / 1.6));
      const ease = 1 - Math.pow(1 - intro, 3);
      ctx.beginPath();
      const steps = 60;
      for (let k = 0; k <= steps * ease; k++) {
        const x = k / steps;
        const y = l.y + Math.sin(x * Math.PI * 2 * l.f + t * l.sp + i) * l.amp - x * .18;
        k ? ctx.lineTo(x * W, y * H) : ctx.moveTo(x * W, y * H);
      }
      ctx.strokeStyle = colors[l.c % colors.length];
      ctx.globalAlpha = l.a;
      ctx.lineWidth = l.w;
      ctx.shadowColor = colors[l.c % colors.length];
      ctx.shadowBlur = 14;
      ctx.stroke();
    });
    ctx.globalAlpha = 1; ctx.shadowBlur = 0;
    if (running && !reduceMotion) requestAnimationFrame(draw);
  }
  resize();
  window.addEventListener("resize", () => { resize(); if (reduceMotion) draw(performance.now()); });
  if ("IntersectionObserver" in window) {
    new IntersectionObserver(([e]) => {
      const was = running; running = e.isIntersecting;
      if (running && !was && !reduceMotion) requestAnimationFrame(draw);
    }).observe(cv);
  }
  requestAnimationFrame(draw);
})();

/* ---------- 規約ページなどで、空欄の項目は「請求があれば開示」と表示 ---------- */
document.querySelectorAll("[data-site-or]").forEach(el => {
  const v = SITE[el.dataset.siteOr];
  el.textContent = v || el.dataset.fallback;
});
