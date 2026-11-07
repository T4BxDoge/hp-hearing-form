/* =========================================================
   店舗・会社の情報はここにまとめています。
   修正はこの SITE の中を書き換えるだけで、ページ全体に反映されます。
   （ページのタイトル・説明文・OGP は index.html の <head> も直してください）
   ========================================================= */
const SITE = {
  name: "株式会社RE.sense",
  url: "https://t4bxdoge.github.io/hp-hearing-form/sites/re-sense/",
  description: "オンラインサロンの運営、ホームページ制作、テレアポ代行",
  // 営業時間を載せるときは、構造化データ用に曜日・開始・終了を入れる
  // 例：[{ days: ["Monday","Tuesday","Wednesday","Thursday","Friday"], opens: "10:00", closes: "19:00" }]
  openingHours: [],
  tel: "",            // 例："092-000-0000"（空なら表示しない）
  address: "",        // 例："福岡県福岡市中央区〇〇1-2-3"（空なら表示しない）
  lineUrl: "https://lin.ee/yh5nDKW", // 公式LINEの友だち追加URL
  lineId: "",         // 例："@abc1234"（空なら表示しない）
  instagram: "",      // 例："https://www.instagram.com/xxxx/"
  formEndpoint: "",   // お問い合わせの送信先（GASのURL）。空ならデモ動作
  gaId: ""            // Googleアナリティクスの測定ID（例："G-XXXXXXX"）。空なら読み込まない
};

/* ---------- 情報の差し込み ---------- */
(function applySite() {
  document.querySelectorAll("[data-site]").forEach(el => {
    const v = SITE[el.dataset.site];
    if (typeof v === "string" && v) el.textContent = v;
  });
  document.querySelectorAll("[data-site-href]").forEach(el => {
    const v = SITE[el.dataset.siteHref];
    if (v) el.href = v;
  });
  // 空の項目は行ごと隠す
  document.querySelectorAll("[data-site-wrap]").forEach(el => {
    el.hidden = !SITE[el.dataset.siteWrap];
  });
  // 住所 → Googleマップ、電話 → 発信
  document.querySelectorAll("[data-site-map]").forEach(el => {
    if (SITE.address) el.href = "https://www.google.com/maps/search/?api=1&query=" + encodeURIComponent(SITE.address);
    el.target = "_blank"; el.rel = "noopener";
  });
  document.querySelectorAll("[data-site-tel]").forEach(el => {
    if (SITE.tel) el.href = "tel:" + SITE.tel.replace(/[^\d+]/g, "");
  });
  const y = document.getElementById("year");
  if (y) y.textContent = new Date().getFullYear();

  // 構造化データ（Google向けの会社情報）
  const ld = {
    "@context": "https://schema.org",
    "@type": "ProfessionalService",
    name: SITE.name,
    url: SITE.url,
    description: SITE.description,
    image: SITE.url + "images/ogp.png",
    sameAs: [SITE.lineUrl, SITE.instagram].filter(Boolean)
  };
  if (SITE.openingHours.length) ld.openingHoursSpecification = SITE.openingHours.map(h => ({ "@type": "OpeningHoursSpecification", dayOfWeek: h.days, opens: h.opens, closes: h.closes }));
  if (SITE.tel) ld.telephone = SITE.tel;
  if (SITE.address) ld.address = { "@type": "PostalAddress", streetAddress: SITE.address, addressCountry: "JP" };
  const ldEl = document.getElementById("ld");
  if (ldEl) ldEl.textContent = JSON.stringify(ld);

  // アクセス解析（IDがあるときだけ）
  if (SITE.gaId) {
    const s = document.createElement("script");
    s.async = true;
    s.src = "https://www.googletagmanager.com/gtag/js?id=" + encodeURIComponent(SITE.gaId);
    document.head.appendChild(s);
    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { dataLayer.push(arguments); };
    gtag("js", new Date());
    gtag("config", SITE.gaId);
  }
})();

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

/* ---------- プライバシーポリシーを開く ---------- */
document.querySelectorAll(".open-privacy").forEach(a => a.addEventListener("click", () => {
  const d = document.getElementById("privacy");
  if (d) d.open = true;
}));

/* ---------- お問い合わせフォーム ---------- */
(function form() {
  const f = document.getElementById("form");
  if (!f) return;
  const field = n => f.elements.namedItem(n);
  const err = document.getElementById("f-err");
  const ok = document.getElementById("f-ok");
  f.addEventListener("submit", async e => {
    e.preventDefault();
    err.hidden = true; ok.hidden = true;
    const missing = [];
    if (!field("name").value.trim()) missing.push("お名前");
    if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(field("email").value.trim())) missing.push("メールアドレス");
    if (!field("message").value.trim()) missing.push("メッセージ");
    if (missing.length) { err.textContent = missing.join("・") + "を入力してください。"; err.hidden = false; return; }
    if (!field("agree").checked) { err.textContent = "プライバシーポリシーへの同意にチェックしてください。"; err.hidden = false; return; }

    if (!SITE.formEndpoint) {
      ok.textContent = "デザインデモのため、このフォームからは送信されません。公開版ではここからお問い合わせが届きます。";
      ok.hidden = false;
      return;
    }
    const btn = f.querySelector("button[type=submit]");
    btn.disabled = true;
    try {
      await fetch(SITE.formEndpoint, {
        method: "POST",
        mode: "no-cors",
        headers: { "Content-Type": "text/plain;charset=utf-8" },
        body: JSON.stringify({ name: field("name").value.trim(), email: field("email").value.trim(), kind: field("kind").value, message: field("message").value.trim() })
      });
      f.reset();
      ok.textContent = "送信しました。内容を確認して、折り返しご連絡します。";
      ok.hidden = false;
    } catch (_) {
      err.textContent = "送信できませんでした。通信状況を確認するか、LINEからご連絡ください。";
      err.hidden = false;
    } finally {
      btn.disabled = false;
    }
  });
})();
