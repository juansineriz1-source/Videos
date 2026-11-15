# Genera g3m.html (Matriz) y g3c.html (Cinético) a partir de g3.html, y renderx.js / armar_look.py a partir del motor.
import re,sys
G=open('g3.html').read()
def rep(s,a,b,n=None):
    c=s.count(a)
    assert c>=1 and (n is None or c==n),(c,a[:70])
    return s.replace(a,b)
FONDO_M=r"""function fondo(t){cx.clearRect(0,0,1080,1920);const band=((t*260)%2400)-240;
 for(let y=20;y<1920;y+=40){const d=Math.abs(y-band),a=.10+(d<200?.22*(1-d/200):0);cx.fillStyle=`rgba(255,255,255,${a})`;for(let x=20;x<1080;x+=40){cx.beginPath();cx.arc(x,y,2.4,0,7);cx.fill()}}}
"""
FONDO_C=r"""function fondo(t){cx.clearRect(0,0,1080,1920);cx.fillStyle='#07060F';cx.fillRect(0,0,1080,1920);cx.globalCompositeOperation='lighter';
 [[ '43,75,255',200,420,.9,.21,.17],['138,43,255',860,1050,.85,.16,.23],['255,90,60',260,1650,.5,.19,.13]].forEach(([c,x,y,a,fx,fy],i)=>{const X=x+Math.sin(t*fx*6.28+i*2)*240,Y=y+Math.cos(t*fy*6.28+i)*200,R=820+Math.sin(t*.5+i)*90;const g=cx.createRadialGradient(X,Y,0,X,Y,R);g.addColorStop(0,`rgba(${c},${a})`);g.addColorStop(.55,`rgba(${c},${a*.35})`);g.addColorStop(1,`rgba(${c},0)`);cx.fillStyle=g;cx.fillRect(0,0,1080,1920)});cx.globalCompositeOperation='source-over'}
"""
FIT=r"""
 // ajuste: nada sin salto de línea se sale del ancho seguro (las letras de estos estilos son más anchas que Anton)
 R.querySelectorAll('.abs,.k,.row,.st').forEach(e=>{const cs=getComputedStyle(e);let f=parseFloat(cs.fontSize),n=0;
  const pasa=()=>cs.whiteSpace==='nowrap'?(e.classList.contains('row')?e.scrollWidth>e.clientWidth+2:(e.style.textAlign==='center'?e.scrollWidth>e.clientWidth+2:e.offsetLeft+e.offsetWidth>1030)):(e.classList.contains('row')&&e.scrollWidth>e.clientWidth+2);
  while(pasa()&&f>22&&n++<80){f-=2;e.style.fontSize=f+'px'}});
"""
def tema(s,T):
    m=T=='m'
    # fuentes
    s=rep(s,"@font-face{font-family:AN;src:url(assets/Anton-Regular.ttf)}","@font-face{font-family:AN;src:url(assets/%s)}@font-face{font-family:NUM;src:url(assets/%s)}"%(("SpaceGrotesk-Bold.ttf","Doto-Black.ttf") if m else ("Unbounded-Black.ttf","Unbounded-Black.ttf")))
    s=rep(s,"@font-face{font-family:MB;src:url(assets/Montserrat-Black.ttf)}","@font-face{font-family:MB;src:url(assets/%s)}"%("SpaceMono-Bold.ttf" if m else "Unbounded-SemiBold.ttf"))
    s=rep(s,"@font-face{font-family:MS;src:url(assets/Montserrat-SemiBold.ttf)}","@font-face{font-family:MS;src:url(assets/SpaceGrotesk-Medium.ttf)}")
    # colores
    s=rep(s,":root{--bg:#070D1A;--bg2:#101B33;--oro:#F2B84B;--ver:#27E08A;--roj:#FF4D57;--bl:#F5F7FB;--gr:#93A4C3}",
          ":root{--bg:#000;--oro:#FFFFFF;--ver:#FFFFFF;--roj:#E5222B;--bl:#FFFFFF;--gr:#9A9A9A;--tin:#000}" if m else ":root{--bg:#07060F;--oro:#D7FF3E;--ver:#3DFFB0;--roj:#FF5A3C;--bl:#FFFFFF;--gr:#C9C6E0;--tin:#07060F}")
    s=rep(s,"const COL={oro:'#F2B84B',ver:'#27E08A',roj:'#FF4D57',gr:'#93A4C3',bl:'#F5F7FB'};",
          "const COL={oro:'#FFFFFF',ver:'#FFFFFF',roj:'#E5222B',gr:'#9A9A9A',bl:'#FFFFFF'};" if m else "const COL={oro:'#D7FF3E',ver:'#3DFFB0',roj:'#FF5A3C',gr:'#C9C6E0',bl:'#FFFFFF'};")
    acc="#FFFFFF" if m else "#D7FF3E"
    s=rep(s,"linear-gradient(90deg,#F2B84B,#FFD98A)",acc); s=rep(s,"linear-gradient(135deg,#F2B84B,#FFD98A)",acc)
    s=s.replace("#0A1226","#000000" if m else "#07060F")
    # fondo
    s,n=re.subn(r"function fondo\(t\)\{.*?\n(?=let key=null)",lambda _:FONDO_M if m else FONDO_C,s,flags=re.S); assert n==1
    # brillos fuera / adaptados
    s=rep(s,"text-shadow:0 0 60px ${col}66,0 10px 40px rgba(0,0,0,.6)","text-shadow:0 8px 30px rgba(0,0,0,.55)")
    s=rep(s,"font-family:AN;line-height:1;white-space:nowrap;color:${col};font-size:320px","font-family:NUM;line-height:1;white-space:nowrap;color:${col};font-size:%dpx;letter-spacing:%s"%((300,"-.02em") if m else (230,"-.04em")))
    s=rep(s,"let f=320;while(N.offsetWidth>900&&f>90)","let f=%d;while(N.offsetWidth>900&&f>70)"%(300 if m else 230))
    s=rep(s,"background:linear-gradient(180deg,${col},${col}55);border-radius:12px 12px 0 0;box-shadow:0 0 50px -6px ${col}99;border-top:6px solid #fff8",
          "background:radial-gradient(circle,${col} 13px,transparent 14.5px) 50% 100%/40px 40px" if m else "background:${j==n-1?col:'rgba(255,255,255,.3)'};border-radius:36px 36px 10px 10px")
    s=rep(s,"white-space:nowrap;font-family:AN;font-size:${n>2?54:68}px;color:${col};text-shadow:0 4px 20px #000","white-space:nowrap;font-family:NUM;font-size:${n>2?%s}px;color:${col};text-shadow:0 4px 20px #000"%("46:60" if m else "34:44"))
    s=rep(s,'style="filter:drop-shadow(0 0 12px ${col})"','style="filter:none"'); s=rep(s,'style="filter:drop-shadow(0 0 14px ${col})"','style="filter:none"')
    if m: s=rep(s,"filter:contrast(1.08) saturate(.85)","filter:grayscale(1) contrast(1.15)")
    s=rep(s,"box-shadow:0 0 60px -8px rgba(242,184,75,.7),0 40px 80px -30px #000","box-shadow:0 40px 80px -30px #000" if m else "box-shadow:0 0 70px -8px rgba(215,255,62,.45),0 40px 80px -30px #000")
    s=rep(s,"border:6px solid var(--oro);border-radius:6px","border:3px solid var(--oro);border-radius:0" if m else "border:6px solid var(--oro);border-radius:34px")
    s=rep(s,"text-shadow:0 0 70px ${col}88,0 10px 40px #000","text-shadow:0 10px 40px #000")
    s=rep(s,"font-family:AN;font-size:160px;line-height:1.03;color:${col}","font-family:NUM;font-size:%dpx;line-height:1.03;color:${col}"%(190 if m else 130))
    s=rep(s,"let f=160;while(B.offsetHeight>480&&f>80)","let f=%d;while((B.offsetHeight>520||B.scrollWidth>B.clientWidth+2)&&f>60)"%(190 if m else 130))
    if m: s=rep(s,"document.body.style.boxShadow=q>0&&(p.color||'roj')==='roj'?`inset 0 0 ${140+70*Math.sin(t*12)}px rgba(255,77,87,.5)`:'none'","")
    else: s=rep(s,"rgba(255,77,87,.5)","rgba(255,90,60,.45)")
    s=rep(s,"color:var(--oro);line-height:.8;text-shadow:0 0 50px rgba(242,184,75,.5)","color:var(--oro);line-height:.8")
    s=rep(s,".row .r{color:var(--oro);white-space:nowrap;font-family:AN;font-size:1.25em;font-weight:400}",".row .r{color:var(--oro);white-space:nowrap;font-family:NUM;font-size:1.2em;font-weight:400}")
    # escena titulo: letras más anchas que Anton
    k=".72" if m else ".58"
    s=rep(s,"font-size:${p.size||170}px;line-height:1.02","font-size:${(p.size||170)*%s}px;line-height:1.04"%k); s=rep(s,"let f=p.size||170;while(h.offsetHeight>620&&f>80)","let f=(p.size||170)*%s;while(h.offsetHeight>640&&f>60)"%k)
    # cierre
    s=rep(s,"""font-family:AN;font-size:140px;line-height:1.02;text-shadow:0 0 60px rgba(242,184,75,.35)">TIEMPO<br><span style="color:var(--oro)">FINANCIERO</span></div>`""",
          ("""font-family:NUM;font-size:200px;line-height:.92">TIEMPO<br><span style="font-family:AN;font-size:100px;letter-spacing:.03em">FINANCIERO<b style="color:var(--roj)">.</b></span></div>`""" if m else
           """font-family:AN;font-size:150px;line-height:1.05">TIEMPO<br><span style="color:var(--oro);font-size:96px">FINANCIERO</span></div>`"""))
    if m: s=rep(s,'left:0;top:700px;width:1080px;text-align:center;font-family:NUM','left:0;top:610px;width:1080px;text-align:center;font-family:NUM')
    # portada y nombres: tamaños
    s=rep(s,"font-family:AN;font-size:150px;line-height:1.04;text-transform:uppercase;text-shadow:0 8px 40px #000\">${p.h}</div>`));let f=150;","font-family:AN;font-size:%dpx;line-height:1.04;text-transform:%s;text-shadow:0 8px 40px #000\">${p.h}</div>`));let f=%d;"%((128,"none",128) if m else (104,"uppercase",104)))
    # ajuste de anchos al final de build
    s=rep(s,"  add(el(`<div class=\"abs\" style=\"left:90px;top:1340px;width:900px;text-align:center;font-size:24px;color:var(--gr)\">Contenido educativo. No es recomendación de inversión.</div>`))}\n}","  add(el(`<div class=\"abs\" style=\"left:90px;top:1340px;width:900px;text-align:center;font-size:24px;color:var(--gr)\">Contenido educativo. No es recomendación de inversión.</div>`))}"+FIT+"}")
    css_m="""
#BG{background:#000}#VG{display:none!important}
#SH{background:linear-gradient(180deg,rgba(0,0,0,.82) 0%,rgba(0,0,0,.5) 30%,rgba(0,0,0,.55) 60%,rgba(0,0,0,.9) 100%)}
.k{color:#9A9A9A;font-family:MB;font-size:30px;letter-spacing:4px}.k:before{display:none}.k span{padding:0}.k span:before{content:"[ ";color:#E5222B}.k span:after{content:" ]";color:#E5222B}
h1{text-transform:none;font-size:104px;line-height:1.04;letter-spacing:-.01em;text-shadow:0 4px 24px rgba(0,0,0,.7)}
b{font-family:NUM;color:#fff;text-transform:uppercase;letter-spacing:-.02em}
.src{font-family:MB;font-size:21px;text-transform:uppercase;letter-spacing:1px}
.row{background:#000;border:0;border-top:2px solid #4a4a4a;border-radius:0;box-shadow:none;font-family:MB;font-size:40px;padding:30px 4px;text-transform:uppercase}.row:after{display:none}
.row.hi{background:#fff;color:#000;padding:30px 26px;justify-content:flex-start}
.st{font-family:MB;font-size:36px;border-width:4px;border-radius:0;background:none}
.fl{border-top-color:#fff;filter:none;border-left-width:24px;border-right-width:24px;border-top-width:30px}
"""
    css_c="""
#BG{background:#07060F}#VG{background:radial-gradient(900px 1300px at 50% 45%,transparent 45%,rgba(7,6,15,.5) 100%)}
#SH{background:linear-gradient(180deg,rgba(20,8,50,.82) 0%,rgba(20,8,50,.4) 30%,rgba(20,8,50,.45) 60%,rgba(7,6,15,.9) 100%)}
.k{font-family:MB;font-size:26px;letter-spacing:1px;color:#fff;height:62px}.k:before{background:rgba(255,255,255,.16);border:2px solid rgba(255,255,255,.45);border-radius:999px;box-shadow:none}.k span{padding:0 28px}
h1{font-size:84px;line-height:1.06;letter-spacing:-.03em}
.src{font-size:22px}
.row{background:rgba(255,255,255,.14);border:2px solid rgba(255,255,255,.38);border-left:2px solid rgba(255,255,255,.38);border-radius:44px;font-family:AN;font-size:34px;padding:34px 44px;box-shadow:none;letter-spacing:-.02em}
.row.hi{background:#D7FF3E;color:#07060F;border-color:#D7FF3E}
.st{font-family:AN;font-size:28px;border-width:4px;border-radius:999px;padding:6px 20px}
.fl{filter:none}
"""
    s=rep(s,"</style></head>",(css_m if m else css_c)+"</style></head>",1)
    s=rep(s,'<div id="R"></div>','<div id="R"></div><div style="position:absolute;left:0;top:0;opacity:0;pointer-events:none"><span style="font-family:AN">a</span><span style="font-family:NUM">a</span><span style="font-family:MB">a</span><span style="font-family:MS">a</span></div>',1)
    return s
open('g3m.html','w').write(tema(G,'m')); open('g3c.html','w').write(tema(G,'c'))
# render: elige el html por look y trata el video real según el estilo
r=open('render3.js').read()
r=rep(r,"C.p.look==='n1'?'n1.html':'g3.html'","({m1:'g3m.html',c3:'g3c.html'})[C.p.look]||'g3.html'")
r=rep(r,"unsharp=5:5:0.5,eq=saturation=0.92:contrast=1.06","unsharp=5:5:0.5,${C.p.look==='m1'?'hue=s=0,eq=contrast=1.14:brightness=0.01':'eq=saturation=1.08:contrast=1.06'}")
r=rep(r,"fps=${fps},eq=saturation=0.85:contrast=1.05[b]","fps=${fps},${C.p.look==='m1'?'hue=s=0,eq=contrast=1.12':'eq=saturation=1.05:contrast=1.05'}[b]")
open('renderx.js','w').write(r)
a=open('armar_tf3.py').read()
a=rep(a,'"render3.js"','"renderx.js"')
a=rep(a,'import json,sys,os,re,subprocess','import json,sys,os,re,subprocess\nLOOK=os.environ["LOOK"]; SUB={"m1":("Space Grotesk Bold",74,"&H2B22E5&","0xE5222B"),"c3":("Unbounded Black",54,"&H3EFFD7&","0xD7FF3E")}[LOOK]')
a=rep(a,"            g=v[2]\n","            g=v[2]; g['look']=LOOK\n")
a=rep(a,'json.dumps({"p":R["portada"],"d":3,"at":{}}','json.dumps({"p":dict(R["portada"],look=LOOK),"d":3,"at":{}}')
a=rep(a,'json.dumps({"p":{"g":"cierre"},','json.dumps({"p":{"g":"cierre","look":LOOK},')
a=rep(a,'"Style: Cap,Montserrat Black,80,&H00FFFFFF,&H00FFFFFF,&H001A0D07,&HB4000000,0,0,0,0,100,100,1,0,1,8,5,2,70,70,340,1"','f"Style: Cap,{SUB[0]},{SUB[1]},&H00FFFFFF,&H00FFFFFF,&H00000000,&HB4000000,0,0,0,0,100,100,0,0,1,7,4,2,70,70,340,1"')
a=rep(a,r'(r"{\c&H4BB8F2&\fscx114\fscy114}"+x[2]+r"{\c&HFFFFFF&\fscx100\fscy100}")',r'(r"{\c"+SUB[2]+r"\fscx110\fscy110}"+x[2]+r"{\c&HFFFFFF&\fscx100\fscy100}")')
a=rep(a,"color=c=0xF2B84B:s={W}x10","color=c={SUB[3]}:s={W}x10")
open('armar_look.py','w').write(a)
print('ok')
