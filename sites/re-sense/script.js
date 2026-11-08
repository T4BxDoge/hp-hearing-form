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
