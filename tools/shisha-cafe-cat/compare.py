import os
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from patterns import P
R=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..','sites','shisha-cafe-cat','patterns')
cards=''.join(f'''<article class="card">
  <div class="card-hd"><span class="no">{n}</span><div><h2>{P[n]["name"]}</h2><p>{P[n]["note"]}</p></div></div>
  <a class="shots" href="{n}/" aria-label="パターン{n}「{P[n]["name"]}」を開く">
    <img class="pc" src="thumbs/{n}-pc.jpg" alt="パターン{n}のPC表示" width="800" height="500" loading="lazy">
    <img class="sp" src="thumbs/{n}-sp.jpg" alt="パターン{n}のスマホ表示" width="390" height="780" loading="lazy">
  </a>
  <div class="links"><a class="open" href="{n}/">パターン{n}を開く</a><a href="{n}/menu.html">メニュー</a><a href="{n}/price.html">料金表</a><a href="{n}/recruit.html">採用情報</a></div>
</article>''' for n in P)
html=f'''<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex">
<title>デザイン案 5パターン｜SHISHA cafe CAT</title>
<style>
:root{{--bg:#f4f4f2;--ink:#1f2023;--muted:#5d6066;--line:#e0e0dd;--card:#fff;color-scheme:light}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--bg);color:var(--ink);font-family:"Hiragino Sans","Noto Sans JP",sans-serif;font-size:16px;line-height:1.8}}
main{{max-width:1100px;margin:0 auto;padding:40px max(16px,env(safe-area-inset-left,0px)) 64px max(16px,env(safe-area-inset-right,0px))}}
h1{{margin:0 0 8px;font-size:clamp(24px,4vw,34px);line-height:1.4}}
.intro{{color:var(--muted);margin:0 0 32px}}
.intro b{{color:var(--ink)}}
.list{{display:grid;gap:24px}}
.card{{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:20px;display:grid;gap:16px}}
.card-hd{{display:flex;gap:14px;align-items:flex-start}}
.no{{flex:none;width:44px;height:44px;border-radius:50%;background:var(--ink);color:#fff;display:grid;place-items:center;font-weight:700;font-size:18px}}
.card h2{{margin:0;font-size:22px;line-height:1.4}}
.card-hd p{{margin:4px 0 0;color:var(--muted)}}
.shots{{display:grid;grid-template-columns:3.2fr 1fr;gap:12px;align-items:start;text-decoration:none}}
.shots img{{display:block;width:100%;height:auto;border:1px solid var(--line);border-radius:8px;transition:transform .3s}}
.shots:hover img{{transform:translateY(-3px)}}
.links{{display:flex;flex-wrap:wrap;gap:8px}}
.links a{{display:inline-flex;align-items:center;min-height:44px;padding:8px 16px;border:1px solid var(--ink);border-radius:8px;text-decoration:none;color:var(--ink)}}
.links .open{{background:var(--ink);color:#fff;font-weight:700}}
@media (min-width:900px){{.list{{grid-template-columns:1fr 1fr}}}}
</style>
</head>
<body>
<main>
<h1>SHISHA cafe CAT　デザイン案（5パターン）</h1>
<p class="intro">ヒアリングの回答をもとに、雰囲気の違う5つのデザインを作りました。どれも<b>トップ・メニュー・料金表・採用情報の4ページ</b>構成で、スマホにも対応しています。画像を押すと、そのパターンが開きます。メニュー・料金・営業時間・住所・電話番号・スタッフ・猫の名前は仮の内容です。</p>
<div class="list">{cards}</div>
</main>
</body>
</html>
'''
open(R+'/index.html','w',encoding='utf-8').write(html)
print('ok')
