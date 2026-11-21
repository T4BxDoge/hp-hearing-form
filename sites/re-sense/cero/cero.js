/* cero のヒーロー演出：2人をつなぐ赤い糸（糸電話）と、舞い散る桜。
   canvas に端末の解像度で毎フレーム描くので、高解像度の画面でもくっきり */
(function ceroFx() {
  const cv = document.getElementById("ceroFx");
  if (!cv || !cv.getContext) return;
  const ctx = cv.getContext("2d");
  const L = document.querySelector(".hero-l"), Rr = document.querySelector(".hero-r");
  const still = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  let W = 0, H = 0, dpr = 1, running = true, a = null, b = null;
  const start = performance.now();
  const petals = Array.from({ length: 26 }, () => newPetal(true));
  function newPetal(any) {
    return { x: Math.random(), y: any ? Math.random() : -0.05, s: 5 + Math.random() * 7, vy: .03 + Math.random() * .04, vx: .01 + Math.random() * .03, r: Math.random() * 6.28, vr: (Math.random() - .5) * 2, ph: Math.random() * 6.28 };
  }
  function resize() {
    const r = cv.getBoundingClientRect();
    dpr = Math.min(window.devicePixelRatio || 1, 3);
    W = r.width; H = r.height;
    cv.width = Math.round(W * dpr); cv.height = Math.round(H * dpr);
    // 糸電話の缶の位置（画像の中の割合）から、糸の両端を決める
    const pt = (img, fx, fy) => {
      if (!img) return null;
      const ir = img.getBoundingClientRect();
      return { x: ir.left - r.left + ir.width * fx, y: ir.top - r.top + ir.height * fy };
    };
    a = pt(L, .87, .42); b = pt(Rr, .08, .47);
  }
  function petal(p) {
    ctx.save();
    ctx.translate(p.x * W, p.y * H);
    ctx.rotate(p.r);
    ctx.beginPath();
    ctx.moveTo(0, -p.s);
    ctx.bezierCurveTo(p.s * .9, -p.s * .6, p.s * .7, p.s * .6, 0, p.s);
    ctx.bezierCurveTo(-p.s * .7, p.s * .6, -p.s * .9, -p.s * .6, 0, -p.s);
    ctx.fillStyle = "rgba(255,196,214,.85)";
    ctx.fill();
    ctx.restore();
  }
  let last = start;
  function draw(now) {
    const t = (now - start) / 1000, dt = Math.min(.05, (now - last) / 1000); last = now;
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    ctx.clearRect(0, 0, W, H);
    // 赤い糸：2人の糸電話の缶から上に弧を描き、真ん中（見出しの上）で蝶結びになる
    if (a && b && W > 0) {
      const grow = still ? 1 : Math.min(1, Math.max(0, (t - .5) / 1.6));
      const ease = 1 - Math.pow(1 - grow, 3);
      const apexY = Math.max(16, Math.min(a.y, b.y) * .25) + (still ? 0 : Math.sin(t * 1.1) * 2);
      const cx = (a.x + b.x) / 2, cy = 2 * apexY - (a.y + b.y) / 2;
      const q = u => ({ x: (1 - u) * (1 - u) * a.x + 2 * (1 - u) * u * cx + u * u * b.x, y: (1 - u) * (1 - u) * a.y + 2 * (1 - u) * u * cy + u * u * b.y });
      ctx.lineCap = "round"; ctx.lineJoin = "round";
      ctx.strokeStyle = "rgba(255,70,70,.95)"; ctx.shadowColor = "#ff2d2d"; ctx.shadowBlur = 12; ctx.lineWidth = 2;
      // 両側の缶から真ん中に向かって伸びる
      [[0, .5], [1, .5]].forEach(([from, to]) => {
        ctx.beginPath();
        for (let k = 0; k <= 40; k++) {
          const u = from + (to - from) * ease * (k / 40);
          const p = q(u);
          k ? ctx.lineTo(p.x, p.y) : ctx.moveTo(p.x, p.y);
        }
        ctx.stroke();
      });
      // 真ん中の蝶結び
      if (grow >= 1) {
        const m = q(.5), sz = Math.max(14, Math.min(28, W * .02));
        const pop = still ? 1 : Math.min(1, (t - 2.1) / .5);
        if (pop > 0) {
          const k = 1 - Math.pow(1 - pop, 3);
          ctx.save(); ctx.translate(m.x, m.y); ctx.scale(k, k);
          ctx.lineWidth = 2.2;
          [-1, 1].forEach(sg => {
            ctx.beginPath();  // 輪
            ctx.moveTo(0, 0);
            ctx.bezierCurveTo(sg * sz * .6, -sz * .9, sg * sz * 1.5, -sz * .5, sg * sz * 1.2, 0);
            ctx.bezierCurveTo(sg * sz * 1.0, sz * .35, sg * sz * .5, sz * .2, 0, 0);
            ctx.stroke();
            ctx.beginPath();  // たれ
            ctx.moveTo(0, 0);
            ctx.quadraticCurveTo(sg * sz * .35, sz * .6, sg * sz * .75, sz * 1.05);
            ctx.stroke();
          });
          ctx.beginPath(); ctx.arc(0, 0, 2.6, 0, 6.29); ctx.fillStyle = "#ff5a5a"; ctx.fill();
          ctx.restore();
        }
      }
      ctx.shadowBlur = 0;
      // 糸の上を行き来する光（会話）
      if (!still && grow >= 1) {
        const u = (Math.sin(t * .9) + 1) / 2, p = q(u);
        const g = ctx.createRadialGradient(p.x, p.y, 0, p.x, p.y, 12);
        g.addColorStop(0, "rgba(255,230,160,1)"); g.addColorStop(1, "rgba(255,120,80,0)");
        ctx.fillStyle = g; ctx.beginPath(); ctx.arc(p.x, p.y, 12, 0, 6.29); ctx.fill();
      }
    }
    // 桜
    petals.forEach((p, i) => {
      if (!still) {
        p.y += p.vy * dt; p.x += (p.vx + Math.sin(t + p.ph) * .01) * dt; p.r += p.vr * dt;
        if (p.y > 1.05 || p.x > 1.05) petals[i] = newPetal(false);
      }
      petal(p);
    });
    if (running && !still) requestAnimationFrame(draw);
  }
  resize();
  window.addEventListener("resize", () => { resize(); if (still) draw(performance.now()); });
  window.addEventListener("load", resize);
  if ("IntersectionObserver" in window) {
    new IntersectionObserver(([e]) => {
      const was = running; running = e.isIntersecting;
      if (running && !was && !still) { last = performance.now(); requestAnimationFrame(draw); }
    }).observe(cv);
  }
  requestAnimationFrame(draw);
})();
