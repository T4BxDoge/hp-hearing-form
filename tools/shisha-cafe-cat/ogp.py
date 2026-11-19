import os
# パターンごとのOGP画像（1200×630）と、比較ページ用のサムネイルを作る
from playwright.sync_api import sync_playwright
R=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..','sites','shisha-cafe-cat','patterns')
STY={
 1:('#ffffff','#1f2023','#f4f4f2','"Noto Sans CJK JP"','猫と、香りと、ひと休み。','700'),
 2:('#fcfcfb','#1c1c1c','#fcfcfb','"Noto Serif CJK JP"','けむりの向こうに、猫がいる。','500'),
 3:('#111111','#ffffff','#1c1c1c','"Noto Sans CJK JP"','すすきので、猫とシーシャ。','900'),
 4:('#f5f3f0','#3a3836','#ffffff','"Noto Sans CJK JP"','ねこと一緒に、ゆっくりシーシャ。','700'),
 5:('#232624','#f4f2ea','#232624','"Noto Sans CJK JP"','本日のおすすめ「猫と一服」','500'),
}
def html(n):
    bg,fg,sub,font,copy,wt=STY[n]
    border='border:18px solid #6b5a46;' if n==5 else ''
    return f'''<!DOCTYPE html><html><head><meta charset="utf-8"><style>
html,body{{margin:0;width:1200px;height:630px;overflow:hidden}}
body{{background:{bg};color:{fg};font-family:{font},sans-serif;{border}box-sizing:border-box;position:relative}}
.in{{position:absolute;left:90px;top:120px;display:grid;gap:26px}}
.en{{font-size:28px;letter-spacing:6px;opacity:.7}}
h1{{margin:0;font-size:{'64' if len(copy)>14 else '76'}px;font-weight:{wt};line-height:1.35;max-width:820px}}
.sub{{font-size:30px;opacity:.75}}
canvas{{position:absolute;right:60px;bottom:40px}}
</style></head><body><div class="in"><div class="en">SHISHA cafe CAT ／ SAPPORO SUSUKINO</div><h1>{copy}</h1><div class="sub">札幌すすきの・猫がいるシーシャカフェ</div></div>
<canvas id="c" width="300" height="300"></canvas><script>
const x=document.getElementById('c').getContext('2d');x.fillStyle='{fg}';x.translate(150,220);x.scale(2.6,2.6);
x.beginPath();x.ellipse(0,0,22,28,0,0,7);x.fill();x.beginPath();x.arc(0,-34,15,0,7);x.fill();
x.beginPath();x.moveTo(-13,-42);x.lineTo(-10,-58);x.lineTo(-2,-46);x.fill();x.beginPath();x.moveTo(13,-42);x.lineTo(10,-58);x.lineTo(2,-46);x.fill();
x.lineWidth=7;x.lineCap='round';x.strokeStyle='{fg}';x.beginPath();x.moveTo(18,20);x.quadraticCurveTo(44,18,40,-8);x.stroke();
</script></body></html>'''
with sync_playwright() as p:
    b=p.chromium.launch()
    for n in range(1,6):
        pg=b.new_page(viewport={'width':1200,'height':630});pg.set_content(html(n));pg.wait_for_timeout(200)
        pg.screenshot(path=f'{R}/{n}/images/ogp.png');pg.close()
    import os; os.makedirs(f'{R}/thumbs',exist_ok=True)
    for n in range(1,6):
        for w,h,dpr,tag in((1280,800,1,'pc'),(390,780,2,'sp')):
            pg=b.new_page(viewport={'width':w,'height':h},device_scale_factor=dpr)
            pg.goto(f'file://{R}/{n}/index.html');pg.wait_for_timeout(3200)
            pg.screenshot(path=f'{R}/thumbs/{n}-{tag}.png');pg.close()
    b.close()
# サムネイルをJPGに縮小（比較ページ用）
from PIL import Image
import glob
for f in glob.glob(os.path.join(R,'thumbs','*.png')):
    im=Image.open(f).convert('RGB'); w=800 if '-pc' in f else 390
    im=im.resize((w,int(im.height*w/im.width))); im.save(f.replace('.png','.jpg'),quality=82,optimize=True); os.remove(f)
print('ok')
