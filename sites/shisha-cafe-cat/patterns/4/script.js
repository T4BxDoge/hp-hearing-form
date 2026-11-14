/* =========================================================
   お店の情報はここにまとめています。
   修正はこの SITE の中を書き換えるだけで、全ページに反映されます。
   （ページのタイトル・説明文・OGP は各HTMLの <head> も直してください）
   ========================================================= */
const SITE = {
  name: "SHISHA cafe CAT",
  url: "https://t4bxdoge.github.io/hp-hearing-form/sites/shisha-cafe-cat/patterns/4/",
  description: "札幌・すすきの周辺で、猫と過ごせるシーシャカフェ",
  hours: "15:00〜翌2:00（L.O. 1:00）",
  holiday: "不定休",
  // 構造化データ用の営業時間（曜日・開始・終了）
  openingHours: [{ days: ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"], opens: "15:00", closes: "02:00" }],
  tel: "011-000-0000",
  address: "札幌市中央区南4条西0丁目0-0 〇〇ビル2F",
  station: "地下鉄南北線 すすきの駅から徒歩3分",
  lineUrl: "https://line.me/R/ti/p/@example",      // 公式LINEの友だち追加URL（仮）
  instagram: "https://www.instagram.com/",        // InstagramのURL（仮）
  gaId: ""                                        // Googleアナリティクスの測定ID。空なら読み込まない
};

const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

/* ---------- 情報の差し込み・構造化データ・アクセス解析 ---------- */
(function applySite() {
  document.querySelectorAll("[data-site]").forEach(el => {
    const v = SITE[el.dataset.site];
    if (typeof v === "string" && v) el.textContent = v;
  });
  document.querySelectorAll("[data-site-href]").forEach(el => {
    const v = SITE[el.dataset.siteHref];
    if (v) el.href = v;
  });
  document.querySelectorAll("[data-site-tel]").forEach(el => {
    if (SITE.tel) el.href = "tel:" + SITE.tel.replace(/[^\d+]/g, "");
  });
  document.querySelectorAll("[data-site-map]").forEach(el => {
    if (SITE.address) el.href = "https://www.google.com/maps/search/?api=1&query=" + encodeURIComponent(SITE.address);
    el.target = "_blank"; el.rel = "noopener";
  });
  const y = document.getElementById("year");
  if (y) y.textContent = new Date().getFullYear();

  const ld = {
    "@context": "https://schema.org",
    "@type": "CafeOrCoffeeShop",
    name: SITE.name,
    url: SITE.url,
    description: SITE.description,
    image: SITE.url + "images/ogp.png",
    telephone: SITE.tel,
    address: { "@type": "PostalAddress", streetAddress: SITE.address, addressLocality: "札幌市", addressRegion: "北海道", addressCountry: "JP" },
    openingHoursSpecification: SITE.openingHours.map(h => ({ "@type": "OpeningHoursSpecification", dayOfWeek: h.days, opens: h.opens, closes: h.closes })),
    sameAs: [SITE.instagram, SITE.lineUrl].filter(Boolean)
  };
  const ldEl = document.getElementById("ld");
  if (ldEl) ldEl.textContent = JSON.stringify(ld);

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

/* ---------- スクロールで現れる演出（画面外の要素だけ隠してから出す） ---------- */
(function reveal() {
  const items = [...document.querySelectorAll(".reveal")];
  if (reduceMotion || !("IntersectionObserver" in window)) { items.forEach(el => el.classList.add("is-in")); return; }
  items.forEach(el => {
    const sibs = [...el.parentElement.children].filter(c => c.classList.contains("reveal"));
    el.style.setProperty("--d", (sibs.indexOf(el) * 0.09) + "s");
  });
  const io = new IntersectionObserver(es => es.forEach(e => {
    if (e.isIntersecting) { e.target.classList.add("is-in"); io.unobserve(e.target); }
  }), { rootMargin: "0px 0px -8% 0px", threshold: 0.12 });
  items.forEach(el => {
    if (el.getBoundingClientRect().top < window.innerHeight) el.classList.add("is-in");
    else { el.classList.add("pre"); io.observe(el); }
  });
})();

/* ---------- ヘッダー（下にスクロールで隠れ、上で出る）・連絡バー ---------- */
(function scrollUi() {
  const hd = document.getElementById("hd");
  const nav = document.getElementById("nav");
  const dock = document.querySelector(".dock");
  let lastY = window.scrollY, ticking = false;
  function update() {
    const y = window.scrollY;
    hd.classList.toggle("is-scrolled", y > 8);
    const open = nav.classList.contains("is-open");
    if (!open && y > 240 && y > lastY + 4) hd.classList.add("is-hidden");
    if (y < lastY - 4 || y < 240) hd.classList.remove("is-hidden");
    if (dock) dock.classList.toggle("is-show", y > 320);
    lastY = y; ticking = false;
  }
  addEventListener("scroll", () => { if (!ticking) { requestAnimationFrame(update); ticking = true; } }, { passive: true });
  update();
})();

/* ---------- スマホのメニュー ---------- */
(function menu() {
  const btn = document.getElementById("burger"), nav = document.getElementById("nav");
  function setOpen(o) {
    nav.classList.toggle("is-open", o);
    btn.setAttribute("aria-expanded", String(o));
    btn.setAttribute("aria-label", o ? "メニューを閉じる" : "メニューを開く");
    document.body.classList.toggle("menu-open", o);
  }
  btn.addEventListener("click", () => setOpen(!nav.classList.contains("is-open")));
  nav.querySelectorAll("a").forEach(a => a.addEventListener("click", () => setOpen(false)));
  addEventListener("keydown", e => { if (e.key === "Escape") setOpen(false); });
  addEventListener("resize", () => { if (innerWidth > 900) setOpen(false); });
})();

/* ---------- PCではLINEボタンをQRコード欄へ（QR画像があるときだけ） ---------- */
(function lineOnPc() {
  const pc = window.matchMedia("(hover: hover) and (pointer: fine) and (min-width: 768px)");
  const img = document.querySelector("#lineQr img");
  if (!img) return;
  const links = [...document.querySelectorAll('[data-site-href="lineUrl"]')].filter(a => !a.closest(".way"));
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

/* ---------- canvas を画面の解像度に合わせて描くための共通処理 ---------- */
function hiDpiCanvas(cv, draw) {
  if (!cv || !cv.getContext) return;
  const ctx = cv.getContext("2d");
  let W = 0, H = 0, dpr = 1, running = true, t0 = performance.now();
  function resize() {
    const r = cv.getBoundingClientRect();
    dpr = Math.min(devicePixelRatio || 1, 3);
    W = r.width; H = r.height;
    cv.width = Math.round(W * dpr); cv.height = Math.round(H * dpr);
  }
  function frame(now) {
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    ctx.clearRect(0, 0, W, H);
    draw(ctx, W, H, reduceMotion ? 4 : (now - t0) / 1000);
    if (running && !reduceMotion) requestAnimationFrame(frame);
  }
  resize();
  addEventListener("resize", () => { resize(); if (reduceMotion) frame(performance.now()); });
  if ("IntersectionObserver" in window) {
    new IntersectionObserver(([e]) => {
      const was = running; running = e.isIntersecting;
      if (running && !was && !reduceMotion) requestAnimationFrame(frame);
    }).observe(cv);
  }
  requestAnimationFrame(frame);
}

/* 猫のシルエット（座った姿）を描く */
function drawCat(ctx, x, y, s, color, tail) {
  ctx.save(); ctx.translate(x, y); ctx.scale(s, s); ctx.fillStyle = color;
  ctx.beginPath(); ctx.ellipse(0, 0, 22, 28, 0, 0, Math.PI * 2); ctx.fill();          // 体
  ctx.beginPath(); ctx.arc(0, -34, 15, 0, Math.PI * 2); ctx.fill();                    // 頭
  ctx.beginPath(); ctx.moveTo(-13, -42); ctx.lineTo(-10, -58); ctx.lineTo(-2, -46); ctx.fill(); // 耳
  ctx.beginPath(); ctx.moveTo(13, -42); ctx.lineTo(10, -58); ctx.lineTo(2, -46); ctx.fill();
  ctx.lineWidth = 7; ctx.lineCap = "round"; ctx.strokeStyle = color;                  // しっぽ
  ctx.beginPath(); ctx.moveTo(18, 20);
  ctx.quadraticCurveTo(44, 18 + (tail || 0) * 6, 40, -8 + (tail || 0) * 10); ctx.stroke();
  ctx.restore();
}

/* 煙のゆらぎ（細い線）を描く */
function drawSmoke(ctx, x, y, h, t, color, width, n) {
  ctx.save(); ctx.strokeStyle = color; ctx.lineWidth = width; ctx.lineCap = "round";
  for (let k = 0; k < n; k++) {
    ctx.beginPath();
    for (let i = 0; i <= 40; i++) {
      const p = i / 40, yy = y - p * h;
      const xx = x + Math.sin(p * 5 + t * 0.9 + k * 1.7) * (6 + p * 26) + k * 6;
      i ? ctx.lineTo(xx, yy) : ctx.moveTo(xx, yy);
    }
    ctx.globalAlpha = 0.5 - k * 0.12; ctx.stroke();
  }
  ctx.restore();
}

/* 看板猫の写真が入る場所に、仮のイラストを描く（写真をもらったら img に差し替え） */
document.querySelectorAll(".cat-ph").forEach(box => {
  const cv = document.createElement("canvas");
  cv.setAttribute("aria-hidden", "true");
  box.appendChild(cv);
  const colors = ["#c98a4b", "#8a8378", "#26262a"];
  const color = colors[+box.dataset.cat % 3];
  hiDpiCanvas(cv, (ctx, W, H, t) => {
    const s = Math.min(W, H) / 150;
    drawCat(ctx, W / 2, H * 0.68, s, color, Math.sin(t * 1.4 + +box.dataset.cat));
  });
});

/* ---------- トップの演出（パターン4：やわらか） ---------- */
(function(){
  const rings = Array.from({length: 9}, (_, i) => ({x: Math.random(), d: Math.random(), r: 14 + Math.random() * 26, v: 0.03 + Math.random() * 0.03}));
  hiDpiCanvas(document.getElementById("heroArt"), (ctx, W, H, t) => {
    // ふわふわ浮かぶ煙の輪
    ctx.lineWidth = 3;
    for (const g of rings) {
      const p = ((g.d + t * g.v) % 1);
      const x = g.x * W + Math.sin(t * 0.6 + g.d * 6) * 20, y = H - p * (H + 60);
      ctx.strokeStyle = "rgba(90,86,82," + (0.18 * (1 - p)) + ")";
      ctx.beginPath(); ctx.ellipse(x, y, g.r * (1 + p * 0.6), g.r * 0.55 * (1 + p * 0.6), 0, 0, Math.PI * 2); ctx.stroke();
    }
    // 足あとが順番に現れる
    const n = 8;
    for (let i = 0; i < n; i++) {
      const ph = ((t * 0.5 - i * 0.25) % 2 + 2) % 2;
      const a = ph < 1 ? Math.min(1, ph * 3) * (1 - ph) : 0;
      if (a <= 0) continue;
      const x = W * 0.08 + i * (W * 0.84 / n), y = H * 0.9 - (i % 2) * 18;
      ctx.fillStyle = "rgba(58,56,54," + (a * 0.35) + ")";
      ctx.beginPath(); ctx.ellipse(x, y, 9, 7, 0, 0, Math.PI * 2); ctx.fill();
      [[-9,-10],[-3,-14],[3,-14],[9,-10]].forEach(([dx, dy]) => { ctx.beginPath(); ctx.arc(x + dx, y + dy, 3.4, 0, Math.PI * 2); ctx.fill(); });
    }
    // 下からのぞく猫
    const peek = reduceMotion ? 1 : (Math.sin(t * 0.8) * 0.5 + 0.5);
    const cx = W * 0.86, cy = H + 18 - peek * 40, s = Math.max(1, W / 600);
    ctx.fillStyle = "#3a3836";
    ctx.beginPath(); ctx.arc(cx, cy, 30 * s, Math.PI, 0); ctx.fill();
    ctx.beginPath(); ctx.moveTo(cx - 26 * s, cy - 8 * s); ctx.lineTo(cx - 22 * s, cy - 38 * s); ctx.lineTo(cx - 6 * s, cy - 26 * s); ctx.fill();
    ctx.beginPath(); ctx.moveTo(cx + 26 * s, cy - 8 * s); ctx.lineTo(cx + 22 * s, cy - 38 * s); ctx.lineTo(cx + 6 * s, cy - 26 * s); ctx.fill();
    ctx.fillStyle = "#fff"; ctx.beginPath(); ctx.arc(cx - 10 * s, cy - 12 * s, 3.5 * s, 0, Math.PI * 2); ctx.arc(cx + 10 * s, cy - 12 * s, 3.5 * s, 0, Math.PI * 2); ctx.fill();
  });
})();
