# Genera n1m.html (escenas de noticias en estilo Matriz) a partir de n1.html por reemplazos. python3 construir_n1.py
s=open('n1.html').read()
def rep(a,b,n=None):
    global s
    c=s.count(a); assert c>0 and (n is None or c==n),(a,c); s=s.replace(a,b)
rep('diseño "papel y marcador" (lab de diseño, 2026-11-14)','estilo MATRIZ (lab de diseño, 2026-11-15; generado por construir_n1.py desde n1.html)')
rep('@font-face{font-family:AN;src:url(fuentes/Anton-Regular.ttf)}','@font-face{font-family:AN;src:url(assets/SpaceGrotesk-Bold.ttf)}@font-face{font-family:NUM;src:url(assets/Doto-Black.ttf)}@font-face{font-family:NUM;src:url(assets/SpaceGrotesk-Bold.ttf);unicode-range:U+25}')
rep('fuentes/Montserrat-Black.ttf','assets/SpaceGrotesk-Bold.ttf')
rep('fuentes/Montserrat-SemiBold.ttf','assets/SpaceGrotesk-Medium.ttf')
rep('fuentes/DMSerifDisplay-Italic.ttf','assets/SpaceGrotesk-Medium.ttf')
rep('fuentes/JetBrainsMono-Bold.ttf','assets/SpaceMono-Bold.ttf')
rep('--noche:#070D1A;--noche2:#0E1830;--oro:#F2B84B;--papel:#F1E7D3;--tinta:#0A1226;--ver:#2FCB85;--roj:#F0525B;--gr:#8FA0BF','--noche:#000;--noche2:#0B0B0B;--oro:#E5222B;--papel:#FFFFFF;--tinta:#000;--ver:#FFFFFF;--roj:#E5222B;--gr:#8A8A8A')
rep("const COL={oro:'#F2B84B',ver:'#2FCB85',roj:'#F0525B',gr:'#8FA0BF',bl:'#F1E7D3'}","const COL={oro:'#E5222B',ver:'#FFFFFF',roj:'#E5222B',gr:'#8A8A8A',bl:'#FFFFFF'}")
# fondo: grilla de puntos en vez de rayas
rep('background:repeating-linear-gradient(90deg,rgba(241,231,211,.045) 0 2px,transparent 2px 90px)','background:radial-gradient(circle,rgba(255,255,255,.16) 2px,transparent 2.6px) 0 0/45px 45px')
rep('background:repeating-linear-gradient(90deg,rgba(10,18,38,.07) 0 2px,transparent 2px 90px)','background:radial-gradient(circle,rgba(0,0,0,.2) 2px,transparent 2.6px) 0 0/45px 45px')
rep('mix-blend-mode:overlay;opacity:.5','mix-blend-mode:overlay;opacity:.22')
# títulos en minúsculas (Space Grotesk), mono se queda en mayúsculas
rep('AN;text-transform:uppercase','AN;letter-spacing:-2px')
rep('#B26A00','#E5222B')
# textos sobre rojo: blancos
rep('color:var(--tinta);background:var(--oro)','color:#fff;background:var(--oro)')
rep('background:var(--oro);color:var(--tinta)','background:var(--oro);color:#fff')
rep('m{position:relative;display:inline-block;color:var(--tinta)','m{position:relative;display:inline-block;color:#fff')
rep('rgba(7,13,26,.85)','rgba(0,0,0,.85)')
rep('rgba(241,231,211','rgba(255,255,255')
rep('rgba(10,18,38','rgba(0,0,0')
rep('rgba(7,13,26','rgba(0,0,0')
# fotos en blanco y negro, sin tinte
rep('filter:saturate(.8) contrast(1.06) brightness(1.04)','filter:grayscale(1) contrast(1.15) brightness(1.02)')
rep('background:#0E1E48;mix-blend-mode:lighten;opacity:.32','display:none')
rep('background:#F2D9A0;mix-blend-mode:multiply;opacity:.2','display:none')
rep('outline:3px solid var(--papel);outline-offset:10px','outline:2px solid var(--papel);outline-offset:10px')
# volanta estilo [ MONO ]
s=s.replace('</style>','''.k{background:none!important;color:#B5B5B5!important;padding:8px 0!important}.k:before{content:"[ ";color:var(--oro)}.k:after{content:" ]";color:var(--oro)}
.papel .k{color:#333!important}
h1{font-size:104px}
</style>''',1)
# refrán y comillas
rep('px/1 SE;color:var(--oro)">“','px/1 AN;color:var(--oro)">“')
rep('px/1.06 SE;color:var(--papel)','px/1.08 MS;letter-spacing:-2px;color:var(--papel)')
rep("hay?100:150}px/1.08","hay?92:136}px/1.08"); rep("encoger(r,hay?230:500,hay?100:150,64)","encoger(r,hay?230:500,hay?92:136,60)")
# números en matriz de puntos
rep('font:620px/1 AN','font:560px/1 NUM')
rep('font:300px/1 AN;white-space:nowrap','font:260px/1 NUM;white-space:nowrap')
rep('let f=300;while','let f=260;while')
# delta: arriba blanco con negro, abajo rojo con blanco
rep("color:var(--tinta);font:60px/84px AN","color:${up?'#000':'#fff'};font:60px/84px AN")
rep("30px solid var(--tinta)","30px solid ${up?'#000':'#fff'}")
rep('font:66px/1.1 SE','font:60px/1.12 MS;letter-spacing:-1px')
rep('font:214px/.98 AN','font:190px/1.1 AN'); rep("transform='rotate(-2deg)'","transform='rotate(0deg)'")
rep('font:150px/1 AN;color:#fff','font:130px/1.1 AN;color:#fff')
# precarga de fuentes
rep('<div id="R"></div>','<div id="R"></div><div style="position:absolute;left:-9999px;opacity:0"><span style="font-family:AN">a</span><span style="font-family:NUM">0</span><span style="font-family:MB">a</span><span style="font-family:MS">a</span><span style="font-family:MO">a</span><span style="font-family:SE">a</span></div>')
open('n1m.html','w').write(s); print('ok',len(s))
