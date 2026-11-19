"""公開前の自動チェック（CLAUDE.md の必須条件10）

使い方:
    python3 tools/check_site.py sites/<slug>            # フォルダ内の全HTMLをチェック
    python3 tools/check_site.py sites/<slug> --shots DIR  # 各 index.html のスマホ・PCのスクショも保存

スマホ（390px）・タブレット（768px）・PC（1280px）で開き、次を確認する。
  - 横スクロールが出ていないか
  - ページ内リンク（#〜）の飛び先があるか
  - 16px未満の文字がないか
  - 44px未満のボタン・リンクがないか（文章中のリンクは除く）
  - h1 が1つだけか
  - コンソールエラーがないか（外部フォントなどの読み込み失敗は除く）
問題がなければ最後に「ALL OK」と出る。
"""
import sys, os, glob
from playwright.sync_api import sync_playwright

JS = '''()=>{
 const r={sw:document.documentElement.scrollWidth,vw:innerWidth};
 r.bad=[...document.querySelectorAll('a[href^="#"]')].map(a=>a.getAttribute('href')).filter(h=>h.length>1&&!document.querySelector(h));
 const small=new Set();
 document.querySelectorAll('body *').forEach(el=>{
   const cs=getComputedStyle(el); if(cs.display==='none'||cs.visibility==='hidden')return;
   if(el.closest('[hidden]')||(el.closest('.nav')&&innerWidth<=900))return;
   const t=[...el.childNodes].some(n=>n.nodeType===3&&n.textContent.trim());
   if(t&&parseFloat(cs.fontSize)<16)small.add(el.tagName+'.'+el.className+':'+el.textContent.trim().slice(0,12));
 });
 r.small=[...small].slice(0,6);
 const tap=[];
 document.querySelectorAll('a,button').forEach(el=>{
   const b=el.getBoundingClientRect(); const cs=getComputedStyle(el);
   if(!b.width||cs.visibility==='hidden'||el.closest('[hidden]'))return;
   if(el.closest('.nav')&&innerWidth<=900)return;
   if(el.closest('p,dd,td,li.way')&&!el.matches('.btn,.way-btn,.tlink'))return;
   if(b.height<44)tap.push((el.textContent||'').trim().slice(0,10)+':'+Math.round(b.height));
 });
 r.tap=tap.slice(0,6); r.h1=document.querySelectorAll('h1').length;
 return r}'''

def main():
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(1)
    root = os.path.abspath(sys.argv[1])
    shots = sys.argv[sys.argv.index("--shots") + 1] if "--shots" in sys.argv else None
    if shots: os.makedirs(shots, exist_ok=True)
    files = sorted(f for f in glob.glob(os.path.join(root, "**", "*.html"), recursive=True))
    ok = True
    with sync_playwright() as p:
        b = p.chromium.launch()
        for f in files:
            rel = os.path.relpath(f, root)
            for w, h in [(390, 844), (768, 1024), (1280, 900)]:
                pg = b.new_page(viewport={"width": w, "height": h})
                errs = []
                pg.on("pageerror", lambda e: errs.append(str(e)))
                pg.on("console", lambda m: m.type == "error" and "ERR_" not in m.text and "Failed to load" not in m.text and errs.append(m.text))
                pg.goto("file://" + f); pg.wait_for_timeout(400)
                r = pg.evaluate(JS)
                prob = []
                if r["sw"] > r["vw"]: prob.append(f"横スクロール {r['sw']}px")
                if r["bad"]: prob.append("リンク先なし " + str(r["bad"]))
                if r["small"]: prob.append("16px未満の文字 " + str(r["small"]))
                if r["tap"]: prob.append("44px未満のボタン " + str(r["tap"]))
                if r["h1"] != 1 and not rel.endswith("patterns/index.html"): prob.append("h1の数 " + str(r["h1"]))
                if errs: prob.append("エラー " + str(errs[:3]))
                if prob:
                    ok = False; print(f"{rel} {w}px: " + " / ".join(prob))
                if shots and os.path.basename(f) == "index.html" and w in (390, 1280):
                    pg.wait_for_timeout(2500)
                    name = rel.replace(os.sep, "_").replace(".html", "") + f"-{w}.png"
                    pg.screenshot(path=os.path.join(shots, name))
                pg.close()
        b.close()
    print("ALL OK" if ok else "問題あり（上の内容を直してから push する）")
    sys.exit(0 if ok else 2)

if __name__ == "__main__":
    main()
