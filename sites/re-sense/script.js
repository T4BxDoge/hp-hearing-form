/* トップページの動き。会社情報・決済リンクは site.js の SITE にまとめています */

const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

/* ---------- 見出し上の英字を1文字ずつ出す ---------- */
document.querySelectorAll("[data-split]").forEach(el => {
  if (reduceMotion) return;
  const text = el.textContent;
  el.setAttribute("aria-label", text);
  el.textContent = "";
  // 単語の途中で折り返さないよう、単語ごとにまとめてから1文字ずつに分ける
  let i = 0;
  text.split(" ").forEach((word, wi, arr) => {
    const w = document.createElement("span");
    w.className = "w";
    w.setAttribute("aria-hidden", "true");
    [...word].forEach(c => {
      const span = document.createElement("span");
      span.className = "ch";
      span.textContent = c;
      span.style.animationDelay = (i++ * 0.018) + "s";
      w.appendChild(span);
    });
    el.appendChild(w);
    if (wi < arr.length - 1) el.appendChild(document.createTextNode(" "));
  });
});

/* ---------- スクロールで現れる演出 ---------- */
(function reveal() {
  const items = [...document.querySelectorAll(".reveal")];
  if (reduceMotion || !("IntersectionObserver" in window)) {
    items.forEach(el => el.classList.add("is-in"));
    return;
  }
  // 同じ親の中で順番に少しずつ遅らせる
  items.forEach(el => {
    const sibs = [...el.parentElement.children].filter(c => c.classList.contains("reveal"));
    el.style.setProperty("--d", (sibs.indexOf(el) * 0.1) + "s");
  });
  const io = new IntersectionObserver(entries => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        e.target.classList.add("is-in");
        io.unobserve(e.target);
      }
    });
  }, { rootMargin: "0px 0px -8% 0px", threshold: 0.12 });
  items.forEach(el => {
    // 最初から画面内にあるものは隠さない（読めない時間を作らない）
    if (el.getBoundingClientRect().top < window.innerHeight) {
      el.classList.add("is-in");
    } else {
      el.classList.add("pre");
      io.observe(el);
    }
  });
})();

/* ---------- ヘッダー・進み具合バー・追従ボタン ---------- */
(function scrollUi() {
  const hd = document.getElementById("hd");
  const bar = document.getElementById("progress");
  const fl = document.querySelector(".float-line");
  const hero = document.querySelector(".hero");
  const nav = document.getElementById("nav");
  let lastY = window.scrollY, ticking = false;
  function update() {
    const y = window.scrollY;
    const max = document.documentElement.scrollHeight - window.innerHeight;
    bar.style.transform = "scaleX(" + (max > 0 ? y / max : 0) + ")";
    hd.classList.toggle("is-scrolled", y > 8);
    const menuOpen = nav.classList.contains("is-open");
    hd.classList.toggle("is-hidden", !menuOpen && y > 240 && y > lastY + 4);
    if (y < lastY - 4) hd.classList.remove("is-hidden");
    const heroBottom = hero.offsetTop + hero.offsetHeight;
    const contact = document.getElementById("contact");
    const nearContact = contact.getBoundingClientRect().top < window.innerHeight * 0.6;
    fl.classList.toggle("is-show", y > heroBottom - 200 && !nearContact);
    lastY = y;
    ticking = false;
  }
  window.addEventListener("scroll", () => {
    if (!ticking) { requestAnimationFrame(update); ticking = true; }
  }, { passive: true });
  update();
})();

/* ---------- PCではLINEボタンを押すとQRコードの欄へ移動 ----------
   LINEの友だち追加URLはPCで開くとQRコードの画面になるため、
   ページ内のQRコードを見せてスマホで読み取ってもらう */
(function lineOnPc() {
  const pc = window.matchMedia("(hover: hover) and (pointer: fine) and (min-width: 768px)");
  const img = document.querySelector("#lineQr img");
  if (!img) return;
  const links = [...document.querySelectorAll('[data-site-href="lineUrl"]')].filter(a => !a.closest(".line-card"));
  function apply() {
    const useQr = pc.matches && img.complete && img.naturalWidth > 0;
    links.forEach(a => {
      if (useQr) { a.href = "#contact"; a.removeAttribute("target"); }
      else { a.href = SITE.lineUrl; a.target = "_blank"; }
    });
  }
  if (img.complete) apply(); else img.addEventListener("load", apply);
  pc.addEventListener("change", apply);
})();

/* ---------- スマホのメニュー ---------- */
(function menu() {
  const btn = document.getElementById("burger");
  const nav = document.getElementById("nav");
  function setOpen(open) {
    nav.classList.toggle("is-open", open);
    btn.setAttribute("aria-expanded", String(open));
    btn.setAttribute("aria-label", open ? "メニューを閉じる" : "メニューを開く");
    document.body.style.overflow = open ? "hidden" : "";
  }
  btn.addEventListener("click", () => setOpen(!nav.classList.contains("is-open")));
  nav.querySelectorAll("a").forEach(a => a.addEventListener("click", () => setOpen(false)));
  document.addEventListener("keydown", e => { if (e.key === "Escape") setOpen(false); });
  window.addEventListener("resize", () => { if (window.innerWidth > 900) setOpen(false); });
})();

/* ---------- ヒーローのグラフィック ----------
   画面の解像度（Retinaなど）に合わせてcanvasに毎フレーム描くので、拡大・回転してもぼやけない */
(function heroArt() {
  const cv = document.getElementById("heroArt");
  if (!cv || !cv.getContext) return;
  const ctx = cv.getContext("2d");
  const css = getComputedStyle(document.documentElement);
  const C = {
    line: "#d2d8dd",
    accent: css.getPropertyValue("--accent").trim() || "#4f7889"
  };
  const hex = C.accent.replace("#", "");
  const rgb = [0, 2, 4].map(i => parseInt(hex.slice(i, i + 2), 16)).join(",");
  let W = 0, dpr = 1, running = true, start = performance.now();

  function resize() {
    const r = cv.getBoundingClientRect();
    dpr = Math.min(window.devicePixelRatio || 1, 3);
    W = r.width;
    cv.width = Math.round(r.width * dpr);
    cv.height = Math.round(r.height * dpr);
  }
  const ease = t => 1 - Math.pow(1 - Math.min(Math.max(t, 0), 1), 3);

  function draw(now) {
    const t = (now - start) / 1000;
    const s = W / 600;              // 600×600 の座標で描く
    ctx.setTransform(dpr * s, 0, 0, dpr * s, 0, 0);
    ctx.clearRect(0, 0, 600, 600);
    ctx.lineCap = "round";

    // 円と十字の線（最初の2.4秒で描かれ、その後ゆっくり回る）
    const rot = reduceMotion ? 0 : (t / 80) * Math.PI * 2;
    const p1 = reduceMotion ? 1 : ease((t - 0.2) / 2.4);
    const p2 = reduceMotion ? 1 : ease((t - 0.6) / 2.4);
    ctx.save();
    ctx.translate(300, 300);
    ctx.rotate(rot);
    ctx.strokeStyle = C.line;
    ctx.lineWidth = 1.2 / s;        // 画面上で常に約1.2pxの線
    [250, 180].forEach(r => {
      ctx.beginPath();
      ctx.arc(0, 0, r, -Math.PI / 2, -Math.PI / 2 + Math.PI * 2 * p1);
      ctx.stroke();
    });
    const L = 280 * p2;
    ctx.beginPath();
    ctx.moveTo(-L, 0); ctx.lineTo(L, 0);
    ctx.moveTo(0, -L); ctx.lineTo(0, L);
    ctx.stroke();
    ctx.restore();

    // 中心から広がる波紋（3本を2秒ずつずらして6秒周期）
    if (!reduceMotion) {
      for (let k = 0; k < 3; k++) {
        const ph = ((t + k * 2) % 6) / 6;
        const r = 8 + ph * 170;
        const a = 0.8 * (1 - ph) * (1 - ph);
        ctx.beginPath();
        ctx.arc(300, 300, r, 0, Math.PI * 2);
        ctx.strokeStyle = "rgba(" + rgb + "," + a.toFixed(3) + ")";
        ctx.lineWidth = 1.5 / s;
        ctx.stroke();
      }
    }

    // 中心の点と、ゆっくり脈打つ輪
    const pulse = reduceMotion ? 0 : (Math.sin(t * Math.PI * 2 / 3) + 1) / 2;
    ctx.beginPath();
    ctx.arc(300, 300, (7 + pulse * 8) / s, 0, Math.PI * 2);
    ctx.fillStyle = "rgba(" + rgb + "," + (0.18 * (1 - pulse)).toFixed(3) + ")";
    ctx.fill();
    ctx.beginPath();
    ctx.arc(300, 300, 7 / s, 0, Math.PI * 2);
    ctx.fillStyle = C.accent;
    ctx.fill();

    if (running && !reduceMotion) requestAnimationFrame(draw);
  }

  resize();
  window.addEventListener("resize", () => { resize(); if (reduceMotion) draw(performance.now()); });
  // 画面外にあるときは止めて電池を節約
  if ("IntersectionObserver" in window) {
    new IntersectionObserver(([e]) => {
      const was = running;
      running = e.isIntersecting;
      if (running && !was && !reduceMotion) requestAnimationFrame(draw);
    }).observe(cv);
  }
  requestAnimationFrame(draw);
})();
