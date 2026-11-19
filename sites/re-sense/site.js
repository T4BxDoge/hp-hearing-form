/* =========================================================
   会社の情報・決済リンクはここにまとめています（全ページ共通）。
   修正はこの SITE の中を書き換えるだけで、ページ全体に反映されます。
   （ページのタイトル・説明文・OGP は各ページの <head> も直してください）
   ========================================================= */
const SITE = {
  name: "株式会社RE.sense",
  url: "https://resense-inc.com/",
  description: "オンラインコミュニティ（リジェコミュニティ・DFS Collective）の運営、ホームページ制作、テレアポ代行",
  // 営業時間を載せるときは、構造化データ用に曜日・開始・終了を入れる
  // 例：[{ days: ["Monday","Tuesday","Wednesday","Thursday","Friday"], opens: "10:00", closes: "19:00" }]
  openingHours: [],
  tel: "",            // 例："092-000-0000"（空なら表示しない）
  address: "",        // 例："福岡県福岡市中央区〇〇1-2-3"（空なら表示しない）
  representative: "", // 代表者名（特定商取引法に基づく表記用。空なら「請求があれば開示」と表示）
  email: "info@resense-inc.com", // お問い合わせ用メールアドレス
  lineUrl: "https://lin.ee/yh5nDKW", // 公式LINEの友だち追加URL
  lineId: "",         // 例："@abc1234"（空なら表示しない）
  instagram: "",      // 例："https://www.instagram.com/xxxx/"
  gaId: "",           // Googleアナリティクスの測定ID（例："G-XXXXXXX"）。空なら読み込まない

  // ---- 入会（Stripe の Payment Link の URL を入れる。空なら「準備中」になる） ----
  stripe: {
    rejeGeneral: "",  // リジェコミュニティ 一般プラン（月額2,200円）例："https://buy.stripe.com/xxxx"
    rejeChannel: "",  // リジェコミュニティ チャンネル作成プラン（月額4,400円）
    dfs: ""           // DFS Collective 月額会員プラン（月額2,999円）
  },
  // 会員さまが自分で解約・カード変更できるページ（Stripe のカスタマーポータルのURL）。空なら表示しない
  stripePortal: "",
  // DFS START（無料の公式LINE）の友だち追加URL。空ならボタンを出さない
  dfsLineUrl: ""
};

/* ---------- 情報の差し込み（全ページ共通） ---------- */
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
  // 住所 → Googleマップ、電話 → 発信、メール → メール作成
  document.querySelectorAll("[data-site-map]").forEach(el => {
    if (!SITE.address) return;
    el.href = "https://www.google.com/maps/search/?api=1&query=" + encodeURIComponent(SITE.address);
    el.target = "_blank"; el.rel = "noopener";
  });
  document.querySelectorAll("[data-site-tel]").forEach(el => {
    if (SITE.tel) el.href = "tel:" + SITE.tel.replace(/[^\d+]/g, "");
  });
  document.querySelectorAll("[data-site-mail]").forEach(el => {
    if (SITE.email) el.href = "mailto:" + SITE.email;
  });
  document.querySelectorAll("[data-year]").forEach(el => { el.textContent = new Date().getFullYear(); });

  // 構造化データ（トップページのみ。Google向けの会社情報）
  const ldEl = document.getElementById("ld");
  if (ldEl) {
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
    if (SITE.email) ld.email = SITE.email;
    if (SITE.address) ld.address = { "@type": "PostalAddress", streetAddress: SITE.address, addressCountry: "JP" };
    ldEl.textContent = JSON.stringify(ld);
  }

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
