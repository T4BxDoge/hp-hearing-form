# SHISHA cafe CAT — 5パターン共通の文章とページ構成
SLUG = "shisha-cafe-cat"
BASE = "https://t4bxdoge.github.io/hp-hearing-form/sites/" + SLUG + "/patterns/{n}/"
NAME = "SHISHA cafe CAT"
DEMO = "デザインデモ｜メニュー・料金・営業時間・住所・電話番号・スタッフ・猫の名前は仮の内容です"

PAGES = {
    "index": {"title": "札幌すすきののシーシャカフェ｜猫がいるお店 SHISHA cafe CAT",
              "desc": "札幌・すすきの周辺で、猫と過ごせるシーシャカフェ「SHISHA cafe CAT」。フレーバーは常時40種類以上。看板猫たちとゆっくりくつろげます。"},
    "menu": {"title": "メニュー｜札幌すすきののシーシャカフェ SHISHA cafe CAT",
             "desc": "SHISHA cafe CATのシーシャフレーバーとドリンクのメニュー。フルーツ・ミント・スイーツ系など常時40種類以上。"},
    "price": {"title": "料金表｜札幌すすきののシーシャカフェ SHISHA cafe CAT",
              "desc": "SHISHA cafe CATの料金表。シーシャ1台の料金、チャージ、フレーバー追加、ドリンクの料金と、猫と過ごすときのルール。"},
    "recruit": {"title": "採用情報｜札幌すすきののシーシャカフェ SHISHA cafe CAT",
                "desc": "SHISHA cafe CATのスタッフ募集。シーシャ・猫が好きな方歓迎。未経験OK、シフトは週2日から相談できます。"},
}
NAV = [("index", "トップ"), ("menu", "メニュー"), ("price", "料金表"), ("recruit", "採用情報")]

def href(page, cur, anchor=""):
    f = "index.html" if page == "index" else page + ".html"
    if page == cur and anchor:
        return "#" + anchor
    return f + ("#" + anchor if anchor else "")

# ---------- 共通パーツ ----------
def sec_head(en, ja, lead=""):
    return (f'<div class="sec-head reveal"><p class="en">{en}</p><h2>{ja}</h2>'
            + (f'<p class="lead">{lead}</p>' if lead else "") + "</div>")

CATS = [("むぎ", "茶トラ・男の子", "人なつっこい案内係。シーシャの台の横で寝ていることが多いです。"),
        ("こはく", "キジ白・女の子", "マイペースなお姉さん。気が向くと膝に乗ってくれます。"),
        ("のり", "黒猫・男の子", "店いちばんの若手。おもちゃを見せると全力で遊びます。")]
STAFF = [("店長　さとう", "シーシャ歴8年。その日の気分に合わせたミックスが得意です。"),
         ("スタッフ　みなみ", "猫たちのお世話担当。猫の性格はなんでも聞いてください。")]

FLAVORS = [
    ("フルーツ", ["ダブルアップル", "グレープ", "ピーチ", "マンゴー", "レモン", "ベリーミックス"]),
    ("ミント", ["ペパーミント", "アイスミント", "スペアミント", "ミントレモン"]),
    ("スイーツ", ["バニラ", "キャラメル", "チョコレート", "ココナッツ", "チーズケーキ"]),
    ("ティー・スパイス", ["チャイ", "アールグレイ", "ジャスミン", "シナモン", "ジンジャー"]),
]
DRINKS = [("ソフトドリンク", "500円〜", "コーラ・ジンジャーエール・オレンジ・ウーロン茶など"),
          ("コーヒー・紅茶", "600円〜", "ホット／アイス。シーシャと合う深煎りコーヒー"),
          ("カクテル", "800円〜", "カシス・ピーチ・ミント系のシーシャに合う一杯"),
          ("ビール・ハイボール", "700円〜", "")]
FOODS = [("ナッツ盛り合わせ", "500円"), ("ポテトフライ", "600円"), ("チョコレート", "400円")]

PRICES = [("シーシャ 1台", "2,000円", "フレーバー2種まで・時間制限なし"),
          ("フレーバー追加", "500円", "3種目以降のミックス"),
          ("台の交換", "1,500円", "途中で別の味に変えるとき"),
          ("チャージ（お一人さま）", "500円", "猫たちのお世話代も含みます"),
          ("ワンドリンク", "500円〜", "ご注文をお願いしています")]
RULES = ["猫を無理に抱っこしたり、追いかけたりしないでください",
         "フラッシュでの撮影はご遠慮ください",
         "猫のおやつは、お店で用意しているものだけをあげてください",
         "煙を猫に向けて吐かないでください。猫が休めるスペースは喫煙席と分けています",
         "20歳未満の方はご利用いただけません"]

HOURS = [("営業時間", '<span data-site="hours">15:00〜翌2:00（L.O. 1:00）</span>'),
         ("定休日", '<span data-site="holiday">不定休</span>'),
         ("住所", '<a data-site-map href="#"><span data-site="address">札幌市中央区南4条西0丁目0-0 〇〇ビル2F</span></a>'),
         ("アクセス", '<span data-site="station">地下鉄南北線 すすきの駅から徒歩3分</span>'),
         ("電話", '<a data-site-tel href="#"><span data-site="tel">011-000-0000</span></a>'),
         ("席数", "16席（ソファ席あり）")]

def contact_block():
    return f'''<section class="sec contact" id="contact" aria-labelledby="contact-title">
  <div class="wrap">
    {sec_head("Contact", "お問い合わせ・ご予約", "ご予約やご質問は、お電話・LINE・InstagramのDMで受け付けています。")}
    <ul class="ways">
      <li class="way reveal"><span class="way-ico" aria-hidden="true">☎</span><span class="way-lb">お電話</span><a class="way-btn" data-site-tel href="#"><span data-site="tel">011-000-0000</span></a><span class="way-note">営業時間中に受け付けています</span></li>
      <li class="way reveal"><span class="way-ico" aria-hidden="true">✉</span><span class="way-lb">LINE</span><a class="way-btn" data-site-href="lineUrl" href="#" target="_blank" rel="noopener">LINEで友だち追加</a><span class="way-note">ご予約・空席確認もLINEでどうぞ</span>
        <figure class="line-qr" id="lineQr"><img src="images/line-qr.png" alt="SHISHA cafe CAT 公式LINEの友だち追加QRコード" width="160" height="160" onerror="this.closest('figure').hidden=true"><figcaption>スマホで読み取って友だち追加</figcaption></figure></li>
      <li class="way reveal"><span class="way-ico" aria-hidden="true">◎</span><span class="way-lb">Instagram</span><a class="way-btn" data-site-href="instagram" href="#" target="_blank" rel="noopener">Instagramを見る</a><span class="way-note">猫たちの写真を毎日投稿しています</span></li>
    </ul>
  </div>
</section>'''

def info_block(cur):
    rows = "".join(f'<div><dt>{a}</dt><dd>{b}</dd></div>' for a, b in HOURS)
    return f'''<section class="sec access" id="access" aria-labelledby="access-title">
  <div class="wrap access-grid">
    <div>
      {sec_head("Access", "営業時間・アクセス")}
      <dl class="info reveal">{rows}</dl>
    </div>
    <div class="map reveal" role="img" aria-label="お店の場所のイメージ">
      <div class="map-pin"><span class="map-dot"></span><b>{NAME}</b></div>
      <a class="map-link" data-site-map href="#" target="_blank" rel="noopener">Googleマップで開く</a>
    </div>
  </div>
</section>'''

def page_index():
    cats = "".join(f'<li class="cat-card reveal"><div class="cat-ph" data-cat="{i}" aria-hidden="true"></div><h3>{n}</h3><p class="cat-tag">{t}</p><p>{d}</p></li>' for i, (n, t, d) in enumerate(CATS))
    staff = "".join(f'<li class="staff reveal"><h3>{n}</h3><p>{d}</p></li>' for n, d in STAFF)
    fl = "".join(f'<li class="fl-cat reveal"><h3>{c}</h3><p>{"・".join(xs[:4])} など</p></li>' for c, xs in FLAVORS)
    pr = "".join(f'<div><dt>{a}</dt><dd>{b}</dd></div>' for a, b, _ in PRICES[:4])
    return f'''<section class="sec about" id="about" aria-labelledby="about-title">
  <div class="wrap about-grid">
    {sec_head("About", "猫と過ごす、すすきのの隠れ家。")}
    <div class="about-body">
      <p class="reveal">SHISHA cafe CATは、札幌・すすきの周辺にある、猫がいるシーシャカフェです。ネオンの街から一本入った静かなビルの2階で、看板猫たちがのんびりお出迎えします。</p>
      <p class="reveal">フレーバーは常時40種類以上。初めての方には、好みの味を聞いてスタッフがおすすめをお作りします。おひとりでも、友だちとでも、気軽に立ち寄ってください。</p>
      <ul class="points">
        <li class="reveal"><b>40+</b><span>フレーバー</span></li>
        <li class="reveal"><b>3匹</b><span>看板猫</span></li>
        <li class="reveal"><b>徒歩3分</b><span>すすきの駅から</span></li>
      </ul>
    </div>
  </div>
</section>

<section class="sec cats" id="cats" aria-labelledby="cats-title">
  <div class="wrap">
    {sec_head("Staff", "看板猫とスタッフ", "猫たちはその日の気分で過ごしています。会えるかどうかは、猫しだいです。")}
    <ul class="cat-list">{cats}</ul>
    <ul class="staff-list">{staff}</ul>
  </div>
</section>

<section class="sec menu-pre" id="menu" aria-labelledby="menu-title">
  <div class="wrap">
    {sec_head("Menu", "シーシャとドリンク", "フルーツ系から甘いスイーツ系まで。ドリンクやおつまみもそろえています。")}
    <ul class="fl-list">{fl}</ul>
    <p class="more reveal"><a class="btn" href="menu.html">メニューをすべて見る</a></p>
  </div>
</section>

<section class="sec price-pre" id="price" aria-labelledby="price-title">
  <div class="wrap price-grid">
    {sec_head("Price", "料金のめやす", "時間制限なしで、ゆっくり過ごせます。")}
    <div class="reveal"><dl class="ptable">{pr}</dl><p class="more"><a class="btn" href="price.html">料金表と店内ルールを見る</a></p></div>
  </div>
</section>

{info_block("index")}

<section class="sec recruit-pre" id="recruit" aria-labelledby="recruit-title">
  <div class="wrap recruit-box reveal">
    {sec_head("Recruit", "一緒に働くスタッフを募集中", "シーシャが好きな方、猫が好きな方、どちらも歓迎です。未経験でも大丈夫です。")}
    <p class="more"><a class="btn" href="recruit.html">採用情報を見る</a></p>
  </div>
</section>

{contact_block()}'''

def sub_hero(en, ja, lead):
    return f'''<section class="page-hero"><div class="wrap"><p class="en">{en}</p><h1>{ja}</h1><p class="lead">{lead}</p></div></section>'''

def page_menu():
    fl = "".join(f'<section class="mgroup reveal"><h3>{c}</h3><ul>{"".join(f"<li>{x}</li>" for x in xs)}</ul></section>' for c, xs in FLAVORS)
    dr = "".join(f'<div><dt>{a}{f"<small>{c}</small>" if c else ""}</dt><dd>{b}</dd></div>' for a, b, c in DRINKS)
    fd = "".join(f'<div><dt>{a}</dt><dd>{b}</dd></div>' for a, b in FOODS)
    return sub_hero("Menu", "メニュー", "シーシャのフレーバーは常時40種類以上。ここでは一部をご紹介します。") + f'''
<section class="sec" aria-labelledby="flavor-title">
  <div class="wrap">
    {sec_head("Flavor", "シーシャ フレーバー", "2種類までのミックスは追加料金なし。迷ったら「おまかせ」もできます。")}
    <div class="mgrid">{fl}</div>
    <div class="recommend reveal"><h3>スタッフのおすすめミックス</h3><ul><li><b>ピーチ × ミント</b>：はじめての方に。甘くてすっきり</li><li><b>チャイ × バニラ</b>：猫とまったりしたい夜に</li><li><b>グレープ × アールグレイ</b>：香りを長く楽しみたい方に</li></ul></div>
  </div>
</section>
<section class="sec" aria-labelledby="drink-title">
  <div class="wrap two-col">
    <div>{sec_head("Drink", "ドリンク")}<dl class="ptable reveal">{dr}</dl></div>
    <div>{sec_head("Food", "おつまみ")}<dl class="ptable reveal">{fd}</dl></div>
  </div>
</section>
{contact_block()}'''

def page_price():
    pr = "".join(f'<tr><th>{a}{f"<small>{c}</small>" if c else ""}</th><td>{b}</td></tr>' for a, b, c in PRICES)
    rules = "".join(f'<li class="reveal">{r}</li>' for r in RULES)
    return sub_hero("Price", "料金表", "時間制限なし。シーシャ1台と、お一人さまごとのチャージ・ワンドリンクをお願いしています。") + f'''
<section class="sec" aria-labelledby="pt-title">
  <div class="wrap">
    {sec_head("Price list", "料金（税込）")}
    <div class="table-wrap reveal"><table class="price-table"><tbody>{pr}</tbody></table></div>
    <div class="example reveal"><h3>2名で1台をシェアした場合のめやす</h3><p>シーシャ 2,000円 ＋ チャージ 500円×2 ＋ ドリンク 500円×2 ＝ <b>4,000円（お一人さま 2,000円）</b></p></div>
  </div>
</section>
<section class="sec rules" aria-labelledby="rules-title">
  <div class="wrap">
    {sec_head("Rules", "猫と過ごすときのお願い", "猫たちが安心して過ごせるように、ご協力をお願いします。")}
    <ol class="rule-list">{rules}</ol>
  </div>
</section>
{contact_block()}'''

def page_recruit():
    rows = [("募集職種", "ホール・シーシャスタッフ"), ("仕事内容", "シーシャの準備と提供、ドリンク作り、接客、猫のお世話（ごはん・トイレ掃除など）"),
            ("給与", "時給 1,100円〜（22時以降は深夜手当あり）"), ("勤務時間", "15:00〜翌2:00の間で、4時間以上・シフト制"),
            ("勤務日数", "週2日〜相談できます"), ("応募条件", "20歳以上の方。未経験OK、猫アレルギーのない方"),
            ("待遇", "交通費支給・まかないドリンク無料・制服貸与")]
    tb = "".join(f"<tr><th>{a}</th><td>{b}</td></tr>" for a, b in rows)
    return sub_hero("Recruit", "採用情報", "シーシャと猫が好きな方、一緒に働きませんか。") + f'''
<section class="sec" aria-labelledby="job-title">
  <div class="wrap">
    {sec_head("Job", "募集要項")}
    <div class="table-wrap reveal"><table class="price-table job-table"><tbody>{tb}</tbody></table></div>
  </div>
</section>
<section class="sec" aria-labelledby="voice-title">
  <div class="wrap">
    {sec_head("Voice", "働いているスタッフの声")}
    <ul class="voice-list"><li class="reveal"><p>「シーシャを作ったことはなかったけど、店長が丁寧に教えてくれて1か月で作れるようになりました。猫たちに癒やされながら働けます。」</p><span>スタッフ　みなみ（仮）</span></li><li class="reveal"><p>「お客さんと好きなフレーバーの話をするのが楽しいです。学校帰りに週2日だけ入っています。」</p><span>スタッフ　けんと（仮）</span></li></ul>
  </div>
</section>
<section class="sec" aria-labelledby="flow-title">
  <div class="wrap">
    {sec_head("Flow", "応募の流れ")}
    <ol class="flow"><li class="reveal"><b>1</b><h3>LINE・電話・DMで連絡</h3><p>「採用の件で」と一言送ってください。</p></li><li class="reveal"><b>2</b><h3>お店で面接</h3><p>実際に猫たちとも会ってもらいます。</p></li><li class="reveal"><b>3</b><h3>採用・研修</h3><p>最初はスタッフと一緒にシフトに入ります。</p></li></ol>
  </div>
</section>
{contact_block()}'''

BODIES = {"index": page_index, "menu": page_menu, "price": page_price, "recruit": page_recruit}

def footer(cur):
    nav = "".join(f'<a href="{href(p, cur)}">{l}</a>' for p, l in NAV)
    return f'''<footer class="ft">
  <div class="wrap ft-in">
    <a class="ft-logo" href="index.html">SHISHA cafe <b>CAT</b></a>
    <nav class="ft-nav" aria-label="フッター">{nav}<a data-site-href="instagram" href="#" target="_blank" rel="noopener">Instagram</a></nav>
    <dl class="animal">
      <div><dt>動物取扱業の表示</dt><dd>事業所名：SHISHA cafe CAT　登録番号：第〇〇〇号（展示）</dd></div>
      <div><dt>登録年月日・有効期間</dt><dd>20XX年〇月〇日〜20XX年〇月〇日</dd></div>
      <div><dt>動物取扱責任者</dt><dd>〇〇〇〇</dd></div>
    </dl>
    <p class="copy">20歳未満の方はご利用いただけません。<br>© <span id="year">2026</span> SHISHA cafe CAT</p>
  </div>
</footer>
<nav class="dock" aria-label="お問い合わせ">
  <a data-site-tel href="#"><span aria-hidden="true">☎</span>電話</a>
  <a data-site-href="lineUrl" href="#" target="_blank" rel="noopener"><span aria-hidden="true">✉</span>LINE</a>
  <a data-site-href="instagram" href="#" target="_blank" rel="noopener"><span aria-hidden="true">◎</span>Instagram</a>
</nav>'''

def header(cur):
    items = "".join(f'<a href="{href(p, cur)}"{" aria-current=\"page\"" if p == cur else ""}>{l}</a>' for p, l in NAV)
    items += f'<a href="{href("index", cur, "access")}">アクセス</a><a class="nav-cta" href="{href("index", cur, "contact")}">ご予約・お問い合わせ</a>'
    return f'''<header class="hd" id="hd">
  <div class="wrap hd-in">
    <a class="logo" href="index.html" aria-label="SHISHA cafe CAT トップへ"><span class="logo-mark" aria-hidden="true"></span>SHISHA cafe <b>CAT</b></a>
    <nav class="nav" id="nav" aria-label="メニュー">{items}</nav>
    <button class="burger" id="burger" type="button" aria-label="メニューを開く" aria-expanded="false" aria-controls="nav"><span></span><span></span><span></span></button>
  </div>
</header>'''
