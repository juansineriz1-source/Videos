#!/usr/bin/env python3
"""Historias de @tiempofinancierok (1080x1920).
  python3 historia_tf.py semana|dia <carpeta_salida>      -> 01-eeuu.jpg y 02-argentina.jpg
  python3 historia_tf.py noticia <salida.jpg> <noticia.json>
semana = variacion del ultimo cierre contra el ultimo cierre de la semana anterior; dia = contra el cierre previo.
Datos: Yahoo Finance (cierres diarios) y dolarapi.com. Si un simbolo falla o esta viejo (mas de 4 dias), se omite la fila.
noticia.json: {"k":"NOTICIA DE LA SEMANA","h":"Titulo con <b>resalte</b>","puntos":["..."],"num":"-12,7 %","num_sub":"la accion en la semana","fuente":"Fuentes: ..."}"""
import sys,json,os,subprocess,urllib.request,datetime,html
AQUI=os.path.dirname(os.path.abspath(__file__)); FONTS=os.environ.get("TF_FONTS",os.path.join(AQUI,"..","motor","assets"))
EEUU=[("S&P 500","^GSPC"),("Nasdaq","^IXIC"),("Nasdaq 100","^NDX"),("Dow Jones","^DJI"),("Russell 2000","^RUT"),("Oro","GC=F"),("Bitcoin","BTC-USD")]
ARG=[("ETF Argentina (ARGT)","ARGT"),("ETF Brasil (EWZ)","EWZ"),("YPF","YPF"),("Galicia","GGAL"),("Banco Macro","BMA"),("Pampa Energía","PAM"),("TGS","TGS"),("Vista","VIST"),("Central Puerto","CEPU"),("MercadoLibre","MELI")]
def get(u): return json.loads(urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":"Mozilla/5.0"}),timeout=40).read())
def serie(t):
    d=get(f"https://query1.finance.yahoo.com/v8/finance/chart/{urllib.request.quote(t)}?range=1mo&interval=1d")["chart"]["result"][0]
    return [(datetime.datetime.fromtimestamp(a,datetime.timezone.utc).date(),b) for a,b in zip(d["timestamp"],d["indicators"]["quote"][0]["close"]) if b]
def fila(nombre,t,modo,hoy):
    try: s=serie(t)
    except Exception as e: print("FALLA",t,e); return None
    if t=="BTC-USD" and modo!="dia": s=[x for x in s if x[0].weekday()<5]   # semana: mismo calendario que la bolsa; dia: contra el día anterior real
    s=[x for x in s if x[0]<hoy] if modo=="dia" or hoy.weekday()>=5 else s
    f,c=s[-1]
    if (hoy-f).days>4: print("VIEJO",t,f); return None
    if modo=="semana": prev=[x for x in s if x[0].isocalendar()[:2]<f.isocalendar()[:2]][-1][1]
    else: prev=s[-2][1]
    return {"n":nombre,"v":c,"p":(c/prev-1)*100,"f":f}
def num(v): 
    s=f"{v:,.0f}" if v>=1000 else f"{v:,.2f}"; return s.replace(",","X").replace(".",",").replace("X",".")
def pct(p):
    p=round(p,1)+0.0
    return ("+" if p>=0 else "−")+f"{abs(p):.1f}".replace(".",",")+" %"
CSS="""@font-face{font-family:AN;src:url(FONTS/Anton-Regular.ttf)}@font-face{font-family:MB;src:url(FONTS/Montserrat-Black.ttf)}@font-face{font-family:MS;src:url(FONTS/Montserrat-SemiBold.ttf)}
*{margin:0;padding:0;box-sizing:border-box}body{width:1080px;height:1920px;overflow:hidden;color:#F5F7FB;font-family:MS;background:radial-gradient(1200px 1000px at 50% 30%,#172B55 0%,#0A1226 55%,#050912 100%);position:relative}
.grid{position:absolute;inset:0;background:linear-gradient(rgba(120,160,255,.06) 2px,transparent 2px) 0 0/100% 96px,linear-gradient(90deg,rgba(120,160,255,.06) 2px,transparent 2px) 0 0/108px 100%}
.w{position:absolute;left:70px;right:70px;top:200px;bottom:250px;overflow:hidden;display:flex;flex-direction:column}
.k{align-self:flex-start;background:linear-gradient(90deg,#F2B84B,#FFD98A);color:#0A1226;font-family:MB;font-size:30px;letter-spacing:5px;padding:12px 22px;border-radius:4px;text-transform:uppercase}
h1{font-family:AN;font-weight:400;font-size:100px;line-height:1.04;text-transform:uppercase;margin:18px 0 6px}h1 b{color:#F2B84B;font-weight:400}h1 i{color:#FF4D57;font-style:normal}
.sub{font-size:30px;color:#93A4C3;margin-bottom:20px}
.rows{flex:1;display:flex;flex-direction:column;justify-content:center;gap:16px}
.r{display:grid;grid-template-columns:1fr auto 250px;align-items:center;gap:22px;background:linear-gradient(135deg,rgba(28,44,82,.92),rgba(14,24,48,.92));border:2px solid rgba(255,255,255,.10);border-left:10px solid var(--c);border-radius:16px;padding:14px 26px}
.r .n{font-family:MB;font-size:40px;text-transform:uppercase;line-height:1.1}.r .v{font-size:32px;color:#93A4C3;font-variant-numeric:tabular-nums}
.r .p{font-family:AN;font-size:64px;color:var(--c);text-align:right;white-space:nowrap}
.c .r{padding:2px 24px}.c .rows{gap:7px}.c .n{font-size:33px}.c .p{font-size:48px}.c .v{font-size:28px}.pie{font-size:24px;color:#93A4C3;line-height:1.35;margin-top:16px}.pie b{color:#F5F7FB}
.dol{display:flex;gap:16px;margin-top:14px}.dol div{flex:1;background:rgba(14,24,48,.9);border:2px solid #F2B84B;border-radius:16px;padding:10px 22px;font-family:MB;font-size:26px;text-transform:uppercase}.dol span{display:block;font-family:AN;font-size:50px;color:#F2B84B}
.marca{margin-top:18px;text-align:center;font-family:MB;font-size:23px;letter-spacing:2px;color:#F2B84B}
ul{list-style:none;display:flex;flex-direction:column;gap:20px;margin-top:10px}li{background:linear-gradient(135deg,rgba(28,44,82,.92),rgba(14,24,48,.92));border-left:10px solid #F2B84B;border-radius:16px;padding:20px 26px;font-size:35px;line-height:1.25}li b{color:#F2B84B}
.big{font-family:AN;font-size:170px;line-height:1;color:#FF4D57;text-shadow:0 0 60px rgba(255,77,87,.4);margin-top:26px}.bigs{font-family:MB;font-size:36px;text-transform:uppercase}"""
def render(body,out):
    h=f"<!doctype html><meta charset=utf-8><style>{CSS.replace('FONTS','file://'+os.path.abspath(FONTS))}</style><body><div class=grid></div><div class=w>{body}<div class=marca>@TIEMPOFINANCIEROK · CONTENIDO EDUCATIVO, NO ES RECOMENDACIÓN DE INVERSIÓN</div></div>"
    tmp=out+".html"; open(tmp,"w").write(h)
    js="const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});await p.goto('file://'+process.argv[1]);await p.evaluate(()=>document.fonts.ready);await p.screenshot({path:process.argv[2],type:'jpeg',quality:92});await b.close()})()"
    subprocess.run(["node","-e",js,os.path.abspath(tmp),os.path.abspath(out)],check=True); os.remove(tmp); print(out)
def tabla(k,h,sub,filas,extra=""):
    rows="".join(f'<div class=r style="--c:{"#27E08A" if round(f["p"],1)>=0 else "#FF4D57"}"><div class=n>{html.escape(f["n"])}</div><div class=v>{num(f["v"])}</div><div class=p>{pct(f["p"])}</div></div>' for f in filas)
    c="c" if len(filas)>8 else ""
    return f"<div class='{c}' style='display:contents'><div class=k>{k}</div><h1>{h}</h1><div class=sub>{sub}</div><div class=rows>{rows}</div>{extra}</div>"
MES="enero febrero marzo abril mayo junio julio agosto septiembre octubre noviembre diciembre".split()
if __name__=="__main__":
    modo=sys.argv[1]
    if modo=="noticia":
        n=json.load(open(sys.argv[3])); b=f"<div class=k>{n['k']}</div><h1 style='font-size:100px'>{n['h']}</h1><div class=rows style='justify-content:flex-start;margin-top:20px'><ul>"+"".join(f"<li>{x}</li>" for x in n["puntos"])+"</ul>"
        if n.get("num"): b+=f"<div class=big>{n['num']}</div><div class=bigs>{n.get('num_sub','')}</div>"
        b+=f"</div><div class=pie>{n.get('fuente','')}</div>"; render(b,sys.argv[2]); sys.exit()
    out=sys.argv[2]; os.makedirs(out,exist_ok=True); hoy=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-3))).date()
    us=[x for x in (fila(n,t,modo,hoy) for n,t in EEUU) if x]; ar=[x for x in (fila(n,t,modo,hoy) for n,t in ARG) if x]
    f=us[0]["f"]; fecha=f"{f.day} de {MES[f.month-1]}"
    k="CIERRE DE LA SEMANA" if modo=="semana" else "CIERRE DE AYER"; sub=(f"Variación de la semana, al cierre del viernes {fecha}" if modo=="semana" else f"Variación del día, cierre del {fecha}")
    render(tabla(k,"Wall <b>Street</b>",sub,us,"<div class=pie>Fuente: Yahoo Finance. Índices en puntos; oro y bitcoin en dólares.</div>"),f"{out}/01-eeuu.jpg")
    extra=""
    try:
        d={x["casa"]:x["venta"] for x in get("https://dolarapi.com/v1/dolares")}
        extra=f'<div class=dol><div>Dólar MEP<span>$ {num(d["bolsa"])}</span></div><div>Contado con liqui<span>$ {num(d["contadoconliqui"])}</span></div></div>'
    except Exception as e: print("sin dolar",e)
    render(tabla(k,"Acciones <b>argentinas</b>",sub+". En Nueva York, en dólares.",ar,extra+"<div class=pie>Fuentes: Yahoo Finance y dolarapi.com.</div>"),f"{out}/02-argentina.jpg")
    json.dump({"modo":modo,"fecha":str(f),"eeuu":[{**x,"f":str(x["f"])} for x in us],"arg":[{**x,"f":str(x["f"])} for x in ar]},open(f"{out}/datos.json","w"),ensure_ascii=False,indent=1)
