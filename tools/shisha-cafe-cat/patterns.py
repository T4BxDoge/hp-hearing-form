# 5パターンそれぞれの書体・トップの見せ方・CSS・トップの演出
P = {}

# ---------------------------------------------------------------- 1 王道
P[1] = dict(
  key="standard", name="王道", note="白とグレーで清潔感のある、いちばんオーソドックスな構成。トップは猫とシーシャのイラストに煙がゆらぐ演出",
  fonts="family=Montserrat:wght@500;700&family=Zen+Kaku+Gothic+New:wght@400;500;700",
  hero='''<section class="hero">
  <div class="wrap hero-in">
    <div class="hero-text">
      <p class="eyebrow">Sapporo Susukino ／ Shisha &amp; Cats</p>
      <h1><span class="ln"><span>猫と、香りと、</span></span><span class="ln"><span>ひと休み。</span></span></h1>
      <p class="hero-lead">札幌・すすきのの、猫がいるシーシャカフェ。<br>看板猫たちと、ゆっくりくつろげます。</p>
      <div class="hero-cta"><a class="btn btn-main" href="#contact">ご予約・お問い合わせ</a><a class="btn btn-sub" href="menu.html">メニューを見る</a></div>
      <dl class="hero-meta"><div><dt>営業</dt><dd data-site="hours">15:00〜翌2:00（L.O. 1:00）</dd></div><div><dt>場所</dt><dd>すすきの駅から徒歩3分</dd></div></dl>
    </div>
    <div class="hero-art"><canvas id="heroArt" aria-hidden="true"></canvas></div>
  </div>
</section>''',
  css='''
:root{--bg:#ffffff;--ink:#1f2023;--muted:#5d6066;--line:#e4e4e2;--accent:#2f3033;--soft:#f4f4f2;
  --font-display:"Zen Kaku Gothic New","Hiragino Sans",sans-serif;--font-body:"Zen Kaku Gothic New","Hiragino Sans",sans-serif;--font-en:"Montserrat",sans-serif;color-scheme:light}
.hd{background:rgba(255,255,255,.94);backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px);border-bottom:1px solid transparent}
.hd.is-scrolled{border-bottom-color:var(--line)}
.logo b{font-family:var(--font-en);letter-spacing:.06em}
.logo-mark{border-radius:50%;background:var(--ink);-webkit-mask:radial-gradient(circle at 50% 62%,#000 58%,transparent 60%);position:relative}
.nav a:not(.nav-cta)::after{content:"";position:absolute;left:12px;right:12px;bottom:8px;height:2px;background:var(--ink);transform:scaleX(0);transform-origin:left;transition:transform .35s}
.nav a:not(.nav-cta):hover::after,.nav a[aria-current="page"]::after{transform:scaleX(1)}
.nav-cta{background:var(--ink);color:var(--bg)!important;border-radius:6px;padding:10px 18px!important;margin-left:8px}
.btn{border-radius:6px}
.btn-main,.more .btn{background:var(--ink);color:var(--bg)}
.btn-main:hover,.more .btn:hover{transform:translateY(-2px);box-shadow:0 10px 24px -12px rgba(0,0,0,.5)}
.btn-sub{border:1px solid var(--ink)}
.btn-sub:hover{background:var(--ink);color:var(--bg)}
.sec:nth-of-type(even){background:var(--soft)}
.sec-head .en{font-size:16px;font-weight:700}
.sec-head .en::before{content:"";display:inline-block;width:24px;height:2px;background:var(--ink);vertical-align:middle;margin-right:10px}
/* トップ */
.hero{border-bottom:1px solid var(--line);overflow:hidden}
.hero-in{display:grid;gap:24px;padding-block:clamp(48px,8vw,96px)}
@media (min-width:900px){.hero-in{grid-template-columns:1.05fr 1fr;align-items:center}}
.hero-text{display:grid;gap:22px;justify-items:start;min-width:0}
.eyebrow{font-family:var(--font-en);font-weight:700;letter-spacing:.08em;color:var(--muted);animation:fadeUp .8s both}
.hero h1{font-size:clamp(38px,6.6vw,68px);font-weight:700;letter-spacing:.04em}
.ln{display:block;overflow:hidden}.ln>span{display:inline-block;animation:lineUp 1s cubic-bezier(.2,.8,.2,1) both}.ln:nth-child(2)>span{animation-delay:.12s}
.hero-lead{color:var(--muted);font-size:17px;animation:fadeUp .9s .3s both}
.hero-cta{display:flex;flex-wrap:wrap;gap:12px;animation:fadeUp .9s .45s both}
.hero-meta{margin:0;display:flex;flex-wrap:wrap;gap:6px 24px;padding-top:16px;border-top:1px solid var(--line);animation:fadeUp .9s .6s both}
.hero-meta div{display:flex;gap:10px}.hero-meta dt{color:var(--muted)}.hero-meta dd{margin:0;font-weight:500}
.hero-art{position:relative;aspect-ratio:1/1;max-width:100%;border-radius:12px;background:var(--soft);overflow:hidden;animation:fadeUp 1s .2s both}
.hero-art canvas{position:absolute;inset:0;width:100%;height:100%}
@keyframes lineUp{from{transform:translateY(105%)}to{transform:none}}
.points{display:flex;flex-wrap:wrap;gap:12px;margin-top:24px}
.points li{flex:1 1 140px;padding:18px;border:1px solid var(--line);background:var(--bg);display:grid}
.points b{font-family:var(--font-en);font-size:28px}
.points span{color:var(--muted)}
.about-grid{display:grid;gap:8px}
@media (min-width:900px){.about-grid{grid-template-columns:1fr 1.2fr;gap:56px}}
.about-body{display:grid;gap:16px;min-width:0}
.cat-ph{border-radius:10px}
.cat-card{transition:transform .4s}.cat-card:hover{transform:translateY(-6px)}
.fl-cat,.mgroup,.way,.flow li{border-radius:10px;background:var(--bg);transition:transform .35s,box-shadow .35s}
.fl-cat:hover,.mgroup:hover,.way:hover{transform:translateY(-4px);box-shadow:0 16px 32px -20px rgba(0,0,0,.35)}
.way-btn{border-radius:6px;transition:background .3s,color .3s}.way-btn:hover{background:var(--ink);color:var(--bg)}
.recruit-box{padding:clamp(28px,5vw,56px);background:var(--bg);border:1px solid var(--line);border-radius:12px}
.recruit-box .sec-head{margin-bottom:0}
.page-hero{background:var(--soft);border-bottom:1px solid var(--line)}
''',
  art='''
hiDpiCanvas(document.getElementById("heroArt"), (ctx, W, H, t) => {
  const s = Math.min(W, H) / 400;
  // テーブル
  ctx.fillStyle = "#e3e3e0"; ctx.fillRect(0, H * 0.78, W, H * 0.22);
  // シーシャ（ボトルとホース）
  const bx = W * 0.38, by = H * 0.78;
  ctx.fillStyle = "#2f3033";
  ctx.beginPath(); ctx.ellipse(bx, by - 34 * s, 34 * s, 36 * s, 0, 0, Math.PI * 2); ctx.fill();
  ctx.fillRect(bx - 5 * s, by - 150 * s, 10 * s, 90 * s);
  ctx.fillRect(bx - 20 * s, by - 160 * s, 40 * s, 12 * s);
  ctx.beginPath(); ctx.moveTo(bx - 14 * s, by - 160 * s); ctx.lineTo(bx + 14 * s, by - 160 * s); ctx.lineTo(bx + 8 * s, by - 182 * s); ctx.lineTo(bx - 8 * s, by - 182 * s); ctx.fill();
  ctx.strokeStyle = "#2f3033"; ctx.lineWidth = 4 * s; ctx.beginPath(); ctx.moveTo(bx + 5 * s, by - 110 * s);
  ctx.bezierCurveTo(bx + 90 * s, by - 120 * s, bx + 60 * s, by - 10 * s, bx + 120 * s, by - 20 * s); ctx.stroke();
  // 炭の赤み
  ctx.fillStyle = "rgba(214,120,70," + (0.55 + Math.sin(t * 2) * 0.2) + ")"; ctx.beginPath(); ctx.arc(bx, by - 186 * s, 6 * s, 0, Math.PI * 2); ctx.fill();
  // 煙
  drawSmoke(ctx, bx, by - 192 * s, H * 0.5, t, "#9a9ca0", 2.2 * s, 3);
  // 猫
  drawCat(ctx, W * 0.74, by - 28 * s, 1.5 * s, "#2f3033", Math.sin(t * 1.6));
});
''')

# ---------------------------------------------------------------- 2 ミニマル
P[2] = dict(
  key="minimal", name="ミニマル", note="余白と明朝体の文字が主役。線と細い煙だけで見せる、静かで上品な構成",
  fonts="family=Jost:wght@300;400;500&family=Shippori+Mincho:wght@500;600&family=Noto+Sans+JP:wght@400;500",
  hero='''<section class="hero">
  <canvas id="heroArt" class="hero-canvas" aria-hidden="true"></canvas>
  <div class="wrap hero-in">
    <p class="eyebrow">SHISHA cafe CAT — Sapporo, Susukino</p>
    <h1><span class="ln"><span>けむりの向こうに、</span></span><span class="ln"><span>猫がいる。</span></span></h1>
    <p class="hero-lead">すすきのの路地を一本入ったビルの2階。<br>シーシャと、三匹の猫と、静かな時間。</p>
    <div class="hero-cta"><a class="tlink" href="#contact">ご予約・お問い合わせ</a><a class="tlink" href="menu.html">メニュー</a></div>
  </div>
</section>''',
  css='''
:root{--bg:#fcfcfb;--ink:#1c1c1c;--muted:#6a6a6a;--line:#e2e2e0;--accent:#6a6a6a;--soft:#f3f3f1;
  --font-display:"Shippori Mincho","Hiragino Mincho ProN",serif;--font-body:"Noto Sans JP","Hiragino Sans",sans-serif;--font-en:"Jost",sans-serif;color-scheme:light}
body{line-height:2.05;letter-spacing:.05em}
.hd{background:rgba(252,252,251,.9);backdrop-filter:blur(6px);-webkit-backdrop-filter:blur(6px)}
.logo{font-family:var(--font-en);font-weight:400;letter-spacing:.12em;font-size:18px}
.logo b{font-weight:500}
.logo-mark{width:10px;height:10px;border-radius:50%;background:var(--ink)}
.nav a{font-family:var(--font-body);color:var(--muted)}
.nav a:hover,.nav a[aria-current="page"]{color:var(--ink)}
.nav a[aria-current="page"]{font-weight:500}
.nav-cta{color:var(--ink)!important;border-bottom:1px solid var(--ink)}
.sec{padding-block:clamp(96px,14vw,180px)}
.sec-head .en{font-size:16px;letter-spacing:.3em;text-transform:uppercase}
.sec-head h2{font-weight:500;letter-spacing:.12em}
.btn{background:none;padding:12px 0;border-bottom:1px solid var(--ink);gap:14px;font-weight:500}
.btn::after{content:"→";transition:transform .35s}
.btn:hover::after{transform:translateX(6px)}
.tlink{display:inline-flex;align-items:center;gap:12px;min-height:48px;text-decoration:none;border-bottom:1px solid var(--ink);font-weight:500}
.tlink::after{content:"→";transition:transform .35s}.tlink:hover::after{transform:translateX(6px)}
/* トップ */
.hero{position:relative;overflow:hidden;border-bottom:1px solid var(--line)}
.hero-canvas{position:absolute;right:0;top:0;width:min(46vw,520px);height:100%;max-width:none}
.hero-in{position:relative;display:grid;gap:28px;justify-items:start;padding-block:clamp(110px,18vw,220px) clamp(96px,14vw,180px)}
.eyebrow{font-family:var(--font-en);letter-spacing:.24em;color:var(--muted);animation:fadeUp 1.2s both}
.hero h1{font-family:var(--font-display);font-weight:500;font-size:clamp(34px,6vw,64px);letter-spacing:.12em;line-height:1.6}
.ln{display:block;overflow:hidden}.ln>span{display:inline-block;animation:blurIn 1.6s cubic-bezier(.2,.8,.2,1) both}.ln:nth-child(2)>span{animation-delay:.3s}
.hero-lead{color:var(--muted);animation:fadeUp 1.4s .6s both}
.hero-cta{display:flex;flex-wrap:wrap;gap:32px;animation:fadeUp 1.4s .8s both}
@keyframes blurIn{from{opacity:0;filter:blur(8px);transform:translateY(12px)}to{opacity:1;filter:none;transform:none}}
@media (max-width:767px){.hero-canvas{width:70vw;opacity:.6}}
.about-grid{display:grid;gap:8px;max-width:760px}
.about-body{display:grid;gap:20px}
.points{display:flex;flex-wrap:wrap;gap:40px;margin-top:24px}
.points li{display:grid}
.points b{font-family:var(--font-en);font-weight:300;font-size:40px;line-height:1.2}
.points span{color:var(--muted)}
.cat-ph{background:var(--soft)}
.cat-card h3,.fl-cat h3,.mgroup h3{font-weight:500;letter-spacing:.1em}
.fl-cat,.mgroup,.way,.flow li{border:0;border-top:1px solid var(--ink);padding:24px 0;background:none}
.way-btn{border:0;border-bottom:1px solid var(--ink);padding:10px 0}
.recommend,.example,.voice-list li{background:none;border-left:1px solid var(--ink);padding:8px 0 8px 24px}
.rule-list li::before{background:none;color:var(--ink);border:1px solid var(--ink)}
.map{background:var(--soft)}
.recruit-box{max-width:760px}
.page-hero h1{font-weight:500;letter-spacing:.14em}
.reveal.pre{transform:translateY(16px)}
.reveal.is-in{transition-duration:1.4s}
''',
  art='''
hiDpiCanvas(document.getElementById("heroArt"), (ctx, W, H, t) => {
  // 細い煙の線がゆっくり立ちのぼり、下に小さな猫の線画
  const x = W * 0.55, y = H * 0.86;
  ctx.save(); ctx.strokeStyle = "#1c1c1c"; ctx.lineWidth = 1; ctx.lineCap = "round";
  for (let k = 0; k < 3; k++) {
    ctx.beginPath();
    const prog = reduceMotion ? 1 : Math.min(1, t / 3);
    for (let i = 0; i <= 60 * prog; i++) {
      const p = i / 60, yy = y - 40 - p * H * 0.7;
      const xx = x + Math.sin(p * 4 + t * 0.5 + k * 2) * (4 + p * 40) + k * 10;
      i ? ctx.lineTo(xx, yy) : ctx.moveTo(xx, yy);
    }
    ctx.globalAlpha = 0.55 - k * 0.15; ctx.stroke();
  }
  ctx.globalAlpha = 1;
  // 線画の猫
  ctx.lineWidth = 1.2; const cx = x + 4, cy = y;
  ctx.beginPath(); ctx.ellipse(cx, cy, 16, 20, 0, 0, Math.PI * 2); ctx.stroke();
  ctx.beginPath(); ctx.arc(cx, cy - 26, 11, 0, Math.PI * 2); ctx.stroke();
  ctx.beginPath(); ctx.moveTo(cx - 9, cy - 32); ctx.lineTo(cx - 7, cy - 44); ctx.lineTo(cx - 2, cy - 35);
  ctx.moveTo(cx + 9, cy - 32); ctx.lineTo(cx + 7, cy - 44); ctx.lineTo(cx + 2, cy - 35); ctx.stroke();
  ctx.beginPath(); ctx.moveTo(cx + 14, cy + 12); ctx.quadraticCurveTo(cx + 34, cy + 8, cx + 30 + Math.sin(t) * 4, cy - 12); ctx.stroke();
  ctx.restore();
});
''')

# ---------------------------------------------------------------- 3 ビジュアル
P[3] = dict(
  key="visual", name="ビジュアル", note="黒の大きなトップに、煙の粒と歩く猫たちが動く大胆な構成。文字も大きく、印象に残す見せ方",
  fonts="family=Dela+Gothic+One&family=Archivo:wght@700;800&family=Noto+Sans+JP:wght@400;700",
  hero='''<section class="hero">
  <canvas id="heroArt" class="hero-canvas" aria-hidden="true"></canvas>
  <div class="wrap hero-in">
    <p class="eyebrow">SHISHA × CAT × SUSUKINO</p>
    <h1><span class="ln"><span>すすきので、</span></span><span class="ln"><span>猫とシーシャ。</span></span></h1>
    <p class="hero-lead">フレーバーは40種類以上。三匹の看板猫が待つ、すすきのの夜の休憩所。</p>
    <div class="hero-cta"><a class="btn btn-w" href="#contact">ご予約はこちら</a><a class="btn btn-o" href="menu.html">メニュー</a></div>
  </div>
</section>
<div class="marquee" aria-hidden="true"><div class="mq"><span>SHISHA</span><span>CAT</span><span>CAFE</span><span>SUSUKINO</span><span>SHISHA</span><span>CAT</span><span>CAFE</span><span>SUSUKINO</span><span>SHISHA</span><span>CAT</span><span>CAFE</span><span>SUSUKINO</span><span>SHISHA</span><span>CAT</span><span>CAFE</span><span>SUSUKINO</span></div></div>''',
  css='''
:root{--bg:#ffffff;--ink:#111111;--muted:#5a5a5a;--line:#dedede;--accent:#111111;--soft:#f1f1f1;--dark:#111111;
  --font-display:"Dela Gothic One","Hiragino Sans",sans-serif;--font-body:"Noto Sans JP","Hiragino Sans",sans-serif;--font-en:"Archivo","Arial Black",sans-serif;color-scheme:light}
.hd{background:var(--dark);color:#fff}
.hd .burger span{background:#fff}
.logo{font-family:var(--font-en);font-weight:800;letter-spacing:.04em}
.logo-mark{border:3px solid #fff;border-radius:50%}
@media (max-width:900px){.nav{background:var(--dark);color:#fff}}
.nav a{font-weight:700}
.nav a:hover,.nav a[aria-current="page"]{color:#bdbdbd}
.nav-cta{background:#fff;color:var(--dark)!important;border-radius:99px;padding:10px 20px!important;margin-left:8px}
.btn{border-radius:99px;font-family:var(--font-body)}
.btn-w{background:#fff;color:var(--dark)}.btn-w:hover{transform:translateY(-3px) rotate(-1deg)}
.btn-o{border:2px solid #fff;color:#fff}.btn-o:hover{background:#fff;color:var(--dark)}
.more .btn{background:var(--dark);color:#fff}.more .btn:hover{transform:translateY(-3px)}
.sec-head .en{font-family:var(--font-en);font-size:clamp(40px,8vw,96px);font-weight:800;letter-spacing:-.01em;line-height:1;color:var(--soft);-webkit-text-stroke:1px #bdbdbd}
.sec-head h2{margin-top:-.4em}
/* 黒いセクション */
.cats,.price-pre,.contact{background:var(--dark);color:#fff;--line:#333;--muted:#b5b5b5;--soft:#1c1c1c}
.cats .sec-head .en,.price-pre .sec-head .en,.contact .sec-head .en{color:#1c1c1c;-webkit-text-stroke:1px #444}
.contact .way{background:#1a1a1a}
.contact .way-btn{border-color:#fff}
.price-pre .more .btn,.cats .more .btn{background:#fff;color:var(--dark)}
/* トップ */
.hero{position:relative;background:var(--dark);color:#fff;overflow:hidden}
.hero-canvas{position:absolute;inset:0;width:100%;height:100%}
.hero-in{position:relative;display:grid;gap:24px;justify-items:start;padding-block:clamp(90px,16vw,200px) clamp(110px,16vw,200px)}
.eyebrow{font-family:var(--font-en);font-weight:800;letter-spacing:.2em;color:#bdbdbd;animation:fadeUp .8s both}
.hero h1{font-family:var(--font-display);font-weight:400;font-size:clamp(44px,9.5vw,120px);line-height:1.15;letter-spacing:.02em}
.ln{display:block;overflow:hidden}.ln>span{display:inline-block;animation:slam .9s cubic-bezier(.2,1.4,.3,1) both}.ln:nth-child(2)>span{animation-delay:.12s}
.hero-lead{max-width:32em;color:#d0d0d0;animation:fadeUp .9s .35s both}
.hero-cta{display:flex;flex-wrap:wrap;gap:12px;animation:fadeUp .9s .5s both}
@keyframes slam{from{transform:translateY(110%) skewY(6deg)}to{transform:none}}
.marquee{background:#fff;color:var(--dark);border-block:2px solid var(--dark);overflow:hidden;white-space:nowrap;padding-block:14px}
.mq{display:inline-flex;gap:40px;animation:mq 22s linear infinite;font-family:var(--font-en);font-weight:800;font-size:clamp(24px,4vw,44px)}
.mq span::after{content:"✦";margin-left:40px}
@keyframes mq{to{transform:translateX(-50%)}}
.about-grid{display:grid;gap:8px}
@media (min-width:900px){.about-grid{grid-template-columns:1fr 1fr;gap:56px}}
.about-body{display:grid;gap:16px;min-width:0}
.points{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-top:20px}
.points li{display:grid;padding:16px 8px;background:var(--dark);color:#fff;text-align:center}
.points b{font-family:var(--font-display);font-size:clamp(22px,4vw,34px);font-weight:400}
.points span{color:#bdbdbd}
.cat-ph{background:#1c1c1c;border-radius:0}
.cat-card{transition:transform .4s}.cat-card:hover{transform:scale(1.02)}
.fl-cat{background:var(--dark);color:#fff;border:0;--muted:#bdbdbd;transition:transform .35s}
.fl-cat:hover{transform:translateY(-6px) rotate(-1deg)}
.mgroup{border:2px solid var(--dark)}
.recruit-box{padding:clamp(28px,6vw,64px);background:var(--dark);color:#fff;--muted:#bdbdbd}
.recruit-box .sec-head .en{color:#1c1c1c;-webkit-text-stroke:1px #444}
.recruit-box .more .btn{background:#fff;color:var(--dark)}
.page-hero{background:var(--dark);color:#fff;--muted:#bdbdbd}
.page-hero h1{font-weight:400}
.page-hero .en{color:#bdbdbd;font-family:var(--font-en);font-weight:800}
.dock{background:var(--dark);color:#fff;--line:#333}
.dock span{color:#fff}
.reveal.pre{transform:translateY(48px)}
''',
  art='''
(function(){
  const P = Array.from({length: 70}, () => ({x: Math.random(), y: Math.random(), r: 30 + Math.random() * 90, v: 0.01 + Math.random() * 0.025, ph: Math.random() * 6.28}));
  hiDpiCanvas(document.getElementById("heroArt"), (ctx, W, H, t) => {
    // 煙の粒
    for (const p of P) {
      const y = ((p.y - t * p.v) % 1 + 1) % 1;
      const x = p.x * W + Math.sin(t * 0.4 + p.ph) * 30;
      const g = ctx.createRadialGradient(x, y * H, 0, x, y * H, p.r);
      g.addColorStop(0, "rgba(255,255,255,0.07)"); g.addColorStop(1, "rgba(255,255,255,0)");
      ctx.fillStyle = g; ctx.beginPath(); ctx.arc(x, y * H, p.r, 0, Math.PI * 2); ctx.fill();
    }
    // 下を歩く猫たち
    const base = H - 6, s = Math.max(0.7, Math.min(W, 900) / 700);
    for (let k = 0; k < 3; k++) {
      const x = ((t * (26 + k * 8) + k * 260) % (W + 200)) - 100;
      ctx.save(); ctx.translate(x, base); ctx.scale(s, s); ctx.fillStyle = "#4a4a4a";
      const step = Math.sin(t * 6 + k) * 3;
      ctx.beginPath(); ctx.ellipse(0, -26, 34, 14, 0, 0, Math.PI * 2); ctx.fill();            // 体
      ctx.beginPath(); ctx.arc(34, -38, 12, 0, Math.PI * 2); ctx.fill();                       // 頭
      ctx.beginPath(); ctx.moveTo(26, -46); ctx.lineTo(28, -60); ctx.lineTo(34, -48); ctx.fill();
      ctx.beginPath(); ctx.moveTo(38, -48); ctx.lineTo(44, -60); ctx.lineTo(44, -44); ctx.fill();
      ctx.fillRect(-24, -18, 6, 18 + step); ctx.fillRect(-10, -18, 6, 18 - step); ctx.fillRect(14, -18, 6, 18 + step); ctx.fillRect(24, -18, 6, 18 - step);
      ctx.strokeStyle = "#4a4a4a"; ctx.lineWidth = 6; ctx.lineCap = "round";
      ctx.beginPath(); ctx.moveTo(-32, -30); ctx.quadraticCurveTo(-56, -40, -50, -64 + Math.sin(t * 2 + k) * 6); ctx.stroke();
      // 目
      const blink = (Math.sin(t * 1.3 + k * 2) > 0.96) ? 0.3 : 2.2;
      ctx.fillStyle = "#e9e3a0"; ctx.beginPath(); ctx.ellipse(38, -40, 2.2, blink, 0, 0, Math.PI * 2); ctx.fill();
      ctx.restore();
    }
  });
})();
''')

# ---------------------------------------------------------------- 4 やわらか
P[4] = dict(
  key="soft", name="やわらか", note="丸みのある書体とカードで、親しみやすくやさしい雰囲気。足あとや煙の輪がふわっと浮かぶ構成",
  fonts="family=Zen+Maru+Gothic:wght@500;700&family=Quicksand:wght@500;700",
  hero='''<section class="hero">
  <div class="wrap">
    <div class="hero-card">
      <canvas id="heroArt" class="hero-canvas" aria-hidden="true"></canvas>
      <div class="hero-in">
        <p class="eyebrow">ようこそ、SHISHA cafe CATへ</p>
        <h1><span class="ln"><span>ねこと一緒に、</span></span><span class="ln"><span>ゆっくりシーシャ。</span></span></h1>
        <p class="hero-lead">すすきのの駅から歩いて3分。<br>三匹の看板猫と、ふんわりいい香りでお待ちしています。</p>
        <div class="hero-cta"><a class="btn btn-main" href="#contact">ご予約・お問い合わせ</a><a class="btn btn-sub" href="#cats">猫たちを見る</a></div>
      </div>
    </div>
  </div>
</section>''',
  css='''
:root{--bg:#ffffff;--ink:#3a3836;--muted:#76726d;--line:#ebe8e4;--accent:#5b5753;--soft:#f5f3f0;--r:24px;
  --font-display:"Zen Maru Gothic","Hiragino Maru Gothic ProN",sans-serif;--font-body:"Zen Maru Gothic","Hiragino Maru Gothic ProN",sans-serif;--font-en:"Quicksand",sans-serif;color-scheme:light}
.hd{background:rgba(255,255,255,.92);backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px)}
.hd.is-scrolled{box-shadow:0 6px 20px -14px rgba(0,0,0,.25)}
.logo{font-weight:700}.logo b{font-family:var(--font-en)}
.logo-mark{border-radius:50%;background:radial-gradient(circle at 30% 35%,var(--ink) 18%,transparent 19%),radial-gradient(circle at 70% 35%,var(--ink) 18%,transparent 19%),radial-gradient(circle at 18% 62%,var(--ink) 14%,transparent 15%),radial-gradient(circle at 82% 62%,var(--ink) 14%,transparent 15%),radial-gradient(ellipse 40% 30% at 50% 74%,var(--ink) 98%,transparent 100%)}
.nav a{border-radius:99px;transition:background .25s}
.nav a:hover,.nav a[aria-current="page"]{background:var(--soft)}
.nav-cta{background:var(--ink);color:#fff!important;margin-left:8px}
.nav-cta:hover{background:#000!important}
.btn{border-radius:99px}
.btn-main,.more .btn{background:var(--ink);color:#fff;box-shadow:0 6px 0 #1f1e1d}
.btn-main:hover,.more .btn:hover{transform:translateY(3px);box-shadow:0 3px 0 #1f1e1d}
.btn-sub{background:var(--soft)}.btn-sub:hover{transform:translateY(-2px)}
.sec-head{justify-items:center;text-align:center}
.sec-head .en{font-family:var(--font-en);font-weight:700;font-size:16px;background:var(--soft);padding:4px 14px;border-radius:99px;color:var(--ink)}
.sec-head .lead{margin-inline:auto}
.more{text-align:center}
/* トップ */
.hero{padding-block:clamp(20px,4vw,40px)}
.hero-card{position:relative;overflow:hidden;border-radius:clamp(24px,4vw,40px);background:var(--soft)}
.hero-canvas{position:absolute;inset:0;width:100%;height:100%}
.hero-in{position:relative;display:grid;gap:20px;justify-items:center;text-align:center;padding:clamp(64px,11vw,130px) 20px clamp(120px,14vw,170px)}
.eyebrow{background:#fff;padding:6px 18px;border-radius:99px;font-weight:700;animation:pop .7s both}
.hero h1{font-weight:700;font-size:clamp(32px,6vw,60px);line-height:1.45}
.ln{display:block}.ln>span{display:inline-block;animation:pop .8s .1s both}.ln:nth-child(2)>span{animation-delay:.22s}
.hero-lead{color:var(--muted);animation:fadeUp .9s .35s both}
.hero-cta{display:flex;flex-wrap:wrap;justify-content:center;gap:12px;animation:fadeUp .9s .5s both}
@keyframes pop{0%{opacity:0;transform:scale(.85) translateY(10px)}60%{opacity:1;transform:scale(1.04)}100%{transform:none}}
.about-grid{display:grid;gap:8px;max-width:820px;margin-inline:auto;text-align:center}
.about-body{display:grid;gap:16px;justify-items:center}
.points{display:flex;flex-wrap:wrap;justify-content:center;gap:12px;margin-top:20px}
.points li{display:grid;width:140px;height:140px;place-content:center;border-radius:50%;background:var(--soft);text-align:center;transition:transform .4s}
.points li:hover{transform:rotate(-6deg) scale(1.05)}
.points b{font-family:var(--font-en);font-size:28px}
.cat-ph{border-radius:var(--r)}
.cat-card{text-align:center;justify-items:center}
.cat-card:hover .cat-ph{animation:wiggle .6s}
@keyframes wiggle{25%{transform:rotate(-2deg)}75%{transform:rotate(2deg)}}
.staff{border:0;background:var(--soft);border-radius:var(--r);padding:24px}
.fl-cat,.mgroup,.way,.flow li,.recommend,.example,.voice-list li{border:0;background:var(--soft);border-radius:var(--r);transition:transform .35s}
.fl-cat:hover,.mgroup:hover,.way:hover{transform:translateY(-6px)}
.way{background:#fff;border:2px solid var(--line)}
.way-btn{border-radius:99px;border:0;background:var(--ink);color:#fff}
.map{border-radius:var(--r)}
.map-link{border-radius:99px}
.recruit-box{text-align:center;padding:clamp(28px,5vw,56px);border-radius:clamp(24px,4vw,40px);background:var(--soft)}
.page-hero{text-align:center}
.page-hero .lead{margin-inline:auto}
.page-hero .en{display:inline-block;background:var(--soft);padding:4px 14px;border-radius:99px;font-family:var(--font-en);font-weight:700;color:var(--ink)}
.price-table{border-radius:var(--r);overflow:hidden;background:var(--soft)}
.price-table th,.price-table td{border-bottom:2px solid #fff}
.reveal.is-in{transition-timing-function:cubic-bezier(.3,1.5,.5,1)}
''',
  art='''
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
''')

# ---------------------------------------------------------------- 5 個性派
P[5] = dict(
  key="unique", name="個性派", note="カフェの黒板メニューがモチーフ。チョーク風の手書き文字と、煙の輪・揺れるしっぽで遊び心を出した構成",
  fonts="family=Yusei+Magic&family=Zen+Kaku+Gothic+New:wght@400;700&family=Special+Elite",
  hero='''<section class="hero">
  <div class="wrap hero-in">
    <div class="board">
      <canvas id="heroArt" class="hero-canvas" aria-hidden="true"></canvas>
      <div class="board-text">
        <p class="eyebrow">TODAY'S SPECIAL</p>
        <h1><span class="ln"><span>本日のおすすめ</span></span><span class="ln"><span>「猫と一服」</span></span></h1>
        <p class="hero-lead">シーシャ1台 ＋ 看板猫3匹 ＋ 時間制限なし。<br>すすきの駅から徒歩3分、ビルの2階で営業中。</p>
      </div>
    </div>
    <div class="hero-side">
      <p class="ticket">No.01<br><b>OPEN</b><br><span data-site="hours">15:00〜翌2:00（L.O. 1:00）</span></p>
      <div class="hero-cta"><a class="btn btn-main" href="#contact">ご予約・お問い合わせ</a><a class="btn btn-sub" href="price.html">料金を見る</a></div>
    </div>
  </div>
</section>''',
  css='''
:root{--bg:#fbfaf7;--ink:#1d1d1b;--muted:#5f5e5a;--line:#dcdad4;--accent:#1d1d1b;--soft:#f0eee9;--board:#232624;--chalk:#f4f2ea;
  --font-display:"Yusei Magic","Zen Kaku Gothic New",sans-serif;--font-body:"Zen Kaku Gothic New","Hiragino Sans",sans-serif;--font-en:"Special Elite","Courier New",monospace;color-scheme:light}
body{background-image:radial-gradient(var(--line) 1px,transparent 1px);background-size:22px 22px}
.hd{background:var(--bg);border-bottom:2px solid var(--ink)}
.logo{font-family:var(--font-display)}.logo b{font-family:var(--font-en)}
.logo-mark{background:var(--ink);border-radius:4px;transform:rotate(-6deg)}
.nav a:hover,.nav a[aria-current="page"]{text-decoration:underline wavy;text-underline-offset:6px}
.nav-cta{border:2px solid var(--ink);margin-left:8px;transform:rotate(-1.5deg)}
.nav-cta:hover{background:var(--ink);color:var(--bg)}
.btn{border:2px solid var(--ink);box-shadow:4px 4px 0 var(--ink);background:var(--bg)}
.btn:hover{transform:translate(2px,2px);box-shadow:2px 2px 0 var(--ink)}
.btn-main,.more .btn{background:var(--ink);color:var(--chalk)}
.sec-head .en{font-family:var(--font-en);font-size:16px;display:inline-block;justify-self:start;border:2px dashed var(--ink);padding:2px 12px;transform:rotate(-2deg)}
.sec-head h2{font-family:var(--font-display);font-weight:400}
/* トップ（黒板） */
.hero-in{display:grid;gap:20px;padding-block:clamp(28px,5vw,56px)}
@media (min-width:900px){.hero-in{grid-template-columns:1fr 280px;align-items:end}}
.board{position:relative;overflow:hidden;background:var(--board);color:var(--chalk);border:12px solid #6b5a46;border-radius:6px;box-shadow:0 18px 36px -24px rgba(0,0,0,.6);min-height:min(78vw,520px);animation:swing 1.2s cubic-bezier(.2,1.3,.4,1) both;transform-origin:top center}
.hero-canvas{position:absolute;inset:0;width:100%;height:100%}
.board-text{position:relative;display:grid;gap:16px;padding:clamp(24px,5vw,56px)}
.eyebrow{font-family:var(--font-en);letter-spacing:.2em;opacity:.8}
.hero h1{font-family:var(--font-display);font-weight:400;font-size:clamp(34px,6.6vw,70px);line-height:1.35}
.ln{display:block}.ln>span{display:inline-block;clip-path:inset(0 100% 0 0);animation:write 1s .2s steps(12) both}.ln:nth-child(2)>span{animation-delay:.7s}
.hero-lead{font-family:var(--font-display);font-size:18px;max-width:28em;animation:fadeUp 1s 1.1s both}
.hero-side{display:grid;gap:16px;justify-items:start}
@media (max-width:767px){.board-text{padding-bottom:150px}}
.ticket{font-family:var(--font-en);border:2px dashed var(--ink);background:var(--bg);padding:16px 20px;transform:rotate(2deg);animation:fadeUp .9s .6s both}
.ticket b{font-size:28px}
.hero-cta{display:flex;flex-wrap:wrap;gap:14px;animation:fadeUp .9s .8s both}
@keyframes write{to{clip-path:inset(0 0 0 0)}}
@keyframes swing{0%{transform:rotate(-3deg) translateY(-20px);opacity:0}60%{transform:rotate(1deg);opacity:1}100%{transform:none}}
.about-grid{display:grid;gap:8px}
@media (min-width:900px){.about-grid{grid-template-columns:1fr 1.3fr;gap:56px}}
.about-body{display:grid;gap:16px;min-width:0}
.points{display:flex;flex-wrap:wrap;gap:12px;margin-top:20px}
.points li{display:grid;padding:14px 18px;border:2px solid var(--ink);background:var(--bg)}
.points li:nth-child(odd){transform:rotate(-2deg)}.points li:nth-child(even){transform:rotate(2deg)}
.points b{font-family:var(--font-display);font-size:26px}
.cat-card{background:#fff;padding:12px 12px 18px;box-shadow:0 10px 24px -18px rgba(0,0,0,.6);transition:transform .35s}
.cat-card:nth-child(1){transform:rotate(-2deg)}.cat-card:nth-child(3){transform:rotate(2deg)}
.cat-card:hover{transform:rotate(0) scale(1.03)}
.cat-ph{background:var(--board)}
.cat-card h3{font-family:var(--font-display);font-weight:400}
.staff{border-top:2px dashed var(--ink)}
.fl-cat,.mgroup{background:var(--board);color:var(--chalk);border:0;--muted:#cfccc2;--line:#4a4d4a}
.fl-cat h3,.mgroup h3{font-family:var(--font-display);font-weight:400}
.ptable>div{border-bottom:2px dotted var(--ink)}
.ptable dd,.price-table td{font-family:var(--font-display);font-weight:400;font-size:20px}
.way,.flow li{border:2px solid var(--ink);background:#fff;box-shadow:5px 5px 0 var(--ink)}
.way-btn{border:2px solid var(--ink)}.way-btn:hover{background:var(--ink);color:var(--chalk)}
.recommend,.example,.voice-list li{background:#fff;border:2px dashed var(--ink)}
.map{border:2px solid var(--ink)}
.recruit-box{padding:clamp(24px,5vw,48px);background:var(--board);color:var(--chalk);border:10px solid #6b5a46;--muted:#cfccc2}
.recruit-box .sec-head .en{border-color:var(--chalk)}
.recruit-box .btn{background:var(--chalk);color:var(--ink);border-color:var(--chalk);box-shadow:4px 4px 0 #000}
.page-hero{background:var(--board);color:var(--chalk);--muted:#cfccc2;border-bottom:10px solid #6b5a46}
.page-hero h1{font-family:var(--font-display);font-weight:400}
.page-hero .en{font-family:var(--font-en);color:var(--chalk)}
.price-table th{font-family:var(--font-body)}
''',
  art='''
(function(){
  const rings = Array.from({length: 6}, (_, i) => ({d: i / 6, r: 16 + i % 3 * 6}));
  hiDpiCanvas(document.getElementById("heroArt"), (ctx, W, H, t) => {
    const chalk = "rgba(244,242,234,";
    // チョークで描いたシーシャ
    const bx = W * 0.82, by = H * 0.92, s = Math.max(0.6, Math.min(W, H) / 520);
    ctx.strokeStyle = chalk + "0.75)"; ctx.lineWidth = 2.4 * s; ctx.lineCap = "round"; ctx.lineJoin = "round";
    ctx.beginPath(); ctx.ellipse(bx, by - 36 * s, 30 * s, 32 * s, 0, 0, Math.PI * 2); ctx.stroke();
    ctx.beginPath(); ctx.moveTo(bx, by - 68 * s); ctx.lineTo(bx, by - 150 * s); ctx.stroke();
    ctx.beginPath(); ctx.moveTo(bx - 16 * s, by - 150 * s); ctx.lineTo(bx + 16 * s, by - 150 * s); ctx.lineTo(bx + 10 * s, by - 170 * s); ctx.lineTo(bx - 10 * s, by - 170 * s); ctx.closePath(); ctx.stroke();
    // 立ちのぼる煙の輪（シーシャならではの「O」の輪）
    for (const g of rings) {
      const p = (g.d + t * 0.06) % 1;
      const x = bx - p * W * 0.25 + Math.sin(p * 6 + t) * 10, y = by - 180 * s - p * H * 0.75;
      ctx.strokeStyle = chalk + (0.55 * (1 - p)) + ")"; ctx.lineWidth = (3 - p * 2) * s;
      ctx.beginPath(); ctx.ellipse(x, y, g.r * s * (1 + p), g.r * 0.45 * s * (1 + p), -0.2, 0, Math.PI * 2); ctx.stroke();
    }
    // 黒板のふちから揺れるしっぽ
    const tx = W * 0.08, ty = H;
    ctx.strokeStyle = chalk + "0.8)"; ctx.lineWidth = 9 * s;
    ctx.beginPath(); ctx.moveTo(tx, ty);
    ctx.bezierCurveTo(tx + 10 * s, ty - 50 * s, tx + 40 * s + Math.sin(t * 1.5) * 20 * s, ty - 70 * s, tx + 30 * s + Math.sin(t * 1.5 + 0.8) * 26 * s, ty - 110 * s); ctx.stroke();
  });
})();
''')
