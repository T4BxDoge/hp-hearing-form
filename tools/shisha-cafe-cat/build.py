import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from content import *
from patterns import P

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "sites", SLUG, "patterns")
HERE = os.path.dirname(__file__)
base_css = open(os.path.join(HERE, "base.css"), encoding="utf-8").read()
core_js = open(os.path.join(HERE, "core.js"), encoding="utf-8").read()

def page_html(n, page):
    p = P[n]; meta = PAGES[page]; base = BASE.format(n=n)
    url = base + ("" if page == "index" else page + ".html")
    body = (p["hero"] + "\n" if page == "index" else "") + BODIES[page]()
    return f'''<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{meta["title"]}</title>
<meta name="description" content="{meta["desc"]}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{NAME}">
<meta property="og:title" content="{meta["title"]}">
<meta property="og:description" content="{meta["desc"]}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{base}images/ogp.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="ja_JP">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#ffffff">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?{p["fonts"]}&display=swap">
<link rel="stylesheet" href="style.css">
<script type="application/ld+json" id="ld"></script>
</head>
<body class="p-{p["key"]} page-{page}">
<div class="demo"><a class="demo-back" href="../">← デザイン案の一覧に戻る</a><span>{DEMO}</span></div>
{header(page)}
<main id="top">
{body}
</main>
{footer(page)}
<script src="script.js"></script>
</body>
</html>
'''

for n in P:
    d = os.path.join(ROOT, str(n)); os.makedirs(os.path.join(d, "images"), exist_ok=True)
    for page in PAGES:
        fn = "index.html" if page == "index" else page + ".html"
        open(os.path.join(d, fn), "w", encoding="utf-8").write(page_html(n, page))
    css = f"/* SHISHA cafe CAT — パターン{n}：{P[n]['name']} */\n" + base_css + "\n/* ===== パターン{0}：{1} ===== */".format(n, P[n]["name"]) + P[n]["css"]
    open(os.path.join(d, "style.css"), "w", encoding="utf-8").write(css)
    js = core_js.replace("__URL__", BASE.format(n=n)) + "\n/* ---------- トップの演出（パターン" + str(n) + "：" + P[n]["name"] + "） ---------- */" + P[n]["art"]
    open(os.path.join(d, "script.js"), "w", encoding="utf-8").write(js)
print("built")
