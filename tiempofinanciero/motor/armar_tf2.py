# Armador v2 de reels @tiempofinancierok. Uso: python3 armar_tf2.py <reel.json> <salida.mp4>  (ver motor/README.md)
# reel.json: {"voz":"voz.wav","palabras":"voz.json","tempo":1.1,"segs":[{"hasta":"palabra_final"|null,"n":cant_palabras,"vis":[["c:ID",peso]|["g:escena",peso]],"cartel":"TXT"}],"cierre":1.8}
import json,sys,os,re,subprocess
R=json.load(open(sys.argv[1])); OUT=sys.argv[2]; W,H,FPS=1080,1920,30; T=R.get("tempo",1.0)
os.makedirs("tmp",exist_ok=True)
def run(a): subprocess.run(a,check=True,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
pal=[[w["start_time"]/T,w["end_time"]/T,w["text"]] for w in json.load(open(R["palabras"]))["original_words"]]
DUR=float(subprocess.check_output(["ffprobe","-v","0","-show_entries","format=duration","-of","csv=p=0",R["voz"]]))/T
tok=lambda t: re.sub(r"[^\wáéíóúñü]","",t.lower())
# cortes por cantidad de palabras de cada segmento
ini=[0]
for s in R["segs"]: ini.append(ini[-1]+len(s["txt"].split()))
if ini[-1]!=len(pal):
    # la voz normaliza números ("2008" -> 1 palabra igual); si no coincide, repartir por letras
    L=lambda t: len(re.sub(r"\W","",t)); tot=sum(L(s["txt"]) for s in R["segs"]); totp=sum(L(p[2]) for p in pal); acc=0; ini=[0]; cum=[0]
    for p in pal: cum.append(cum[-1]+L(p[2]))
    for s in R["segs"]: acc+=L(s["txt"]); ini.append(min(range(len(pal)+1),key=lambda j:abs(cum[j]/totp-acc/tot)))
    ini[-1]=len(pal); print("AVISO: palabras no coinciden, alineado por letras")
cortes=[0.0]+[pal[j][0]-0.06 for j in ini[1:-1]]+[DUR+0.25]
partes=[];cuts=[];k=0
for i,s in enumerate(R["segs"]):
    a,b=cortes[i],cortes[i+1]; tw=sum(v[1] for v in s["vis"]); t0=a
    for v in s["vis"]:
        vis,peso=v[0],v[1]
        d=(b-a)*peso/tw; p=f"tmp/p{k}.mp4"; k+=1; cuts.append(t0)
        if vis=="g":
            at={}
            for j in range(ini[i],ini[i+1]): at.setdefault(tok(pal[j][2]),max(0,pal[j][0]-t0))
            run(["node","render2.js",p,f"{d:.3f}",json.dumps({"p":v[2],"d":d,"at":at},ensure_ascii=False)])
        elif vis.startswith("g:"):
            at={}
            for j in range(ini[i],ini[i+1]): at.setdefault(tok(pal[j][2]),max(0,pal[j][0]-t0))
            run(["node","render.js",p,f"{d:.3f}",json.dumps({"g":vis[2:],"d":d,"at":at},ensure_ascii=False)])
        else:
            c,_,ss=vis[2:].partition("@"); z=f"(1+0.05*t/{d:.3f})"
            run(["ffmpeg","-y","-ss",ss or "0.5","-i",f"clips/{c}.mp4","-vf",
              f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},setsar=1,fps={FPS},scale=w='trunc({W}*{z}/2)*2':h=-2:eval=frame,crop={W}:{H},eq=brightness=-0.04:saturation=0.9",
              "-t",f"{d:.3f}","-an","-c:v","libx264","-preset","veryfast","-crf","16","-pix_fmt","yuv420p",p])
        partes.append(p); t0+=d
if R.get("portada"):
    run(["node","render2.js",OUT.replace(".mp4","-portada.png"),"1",json.dumps({"p":R["portada"],"d":1,"at":{}},ensure_ascii=False)])
if R.get("cierre"):
    p=f"tmp/p{k}.mp4"; run(["node","render2.js",p,str(R["cierre"]),json.dumps({"p":{"g":"cierre"},"d":R["cierre"],"at":{}})]); partes.append(p); cuts.append(cortes[-1])
TOT=cortes[-1]+R.get("cierre",0)
open("tmp/l.txt","w").write("".join(f"file '{os.path.abspath(p)}'\n" for p in partes))
run(["ffmpeg","-y","-f","concat","-safe","0","-i","tmp/l.txt","-c","copy","tmp/mudo.mp4"])
# subtítulos palabra por palabra + carteles
def tc(x): x=max(0,x); return f"{int(x//3600)}:{int(x%3600//60):02d}:{x%60:05.2f}"
ass=["[Script Info]","ScriptType: v4.00+","PlayResX: 1080","PlayResY: 1920","WrapStyle: 0","","[V4+ Styles]",
"Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding",
"Style: Cap,Montserrat Black,78,&H00FFFFFF,&H00FFFFFF,&H00261409,&H96000000,0,0,0,0,100,100,1,0,1,7,4,2,70,70,330,1",
"Style: Car,Anton,150,&H00FFFFFF,&H00FFFFFF,&H00261409,&H96000000,0,0,0,0,100,100,2,0,1,8,6,8,70,70,330,1",
"","[Events]","Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text"]
for i,s in enumerate(R["segs"]):
    if s.get("cartel"):
        a=cortes[i]+s.get("cartel_en",0.1); ass.append(f"Dialogue: 1,{tc(a)},{tc(cortes[i+1]-0.05)},Car,,0,0,0,,"+r"{\fad(0,120)\fscx150\fscy150\t(0,200,0.6,\fscx100\fscy100)\c&H4CB6E8&}"+s["cartel"])
    g=[]
    def volcar(g,fin):
        for m,(a,b,w) in enumerate(g):
            e=g[m+1][0] if m+1<len(g) else min(b+0.25,fin)
            txt=" ".join(((r"{\c&H4CB6E8&\fscx112\fscy112}"+x[2]+r"{\c&HFFFFFF&\fscx100\fscy100}") if n==m else x[2]) for n,x in enumerate(g)).upper()
            ass.append(f"Dialogue: 0,{tc(a)},{tc(e)},Cap,,0,0,0,,"+(r"{\fad(50,0)}" if m==0 else "")+txt)
    for j in range(ini[i],ini[i+1]):
        g.append(pal[j])
        if len(g)>=3 or sum(len(x[2]) for x in g)>=13 or pal[j][2][-1] in ".?!:":
            volcar(g,pal[j+1][0] if j+1<len(pal) else DUR+0.2); g=[]
    if g: volcar(g,cortes[i+1])
open("tmp/s.ass","w").write("\n".join(ass)+"\n")
# audio: voz acelerada + whoosh en cada corte + cama grave suave
cs=cuts[1:]; n=len(cs)
run(["ffmpeg","-y","-f","lavfi","-i","anoisesrc=d=0.35:c=pink:a=0.6","-af","highpass=f=600,lowpass=f=5000,afade=t=in:d=0.12,afade=t=out:st=0.12:d=0.23,volume=0.22","tmp/wh.wav"])
fa=f"[1:a]atempo={T},loudnorm=I=-15:TP=-1.5,apad=pad_dur={R.get('cierre',0)+0.5}[vz];[2:a]asplit={n}"+"".join(f"[w{q}]" for q in range(n))+";"+"".join(f"[w{q}]adelay={int(max(0,c-0.15)*1000)}:all=1[d{q}];" for q,c in enumerate(cs))+"[vz]"+"".join(f"[d{q}]" for q in range(n))+f"amix=inputs={n+1}:normalize=0:duration=first[a]"
fv=f"[0:v]ass=tmp/s.ass:fontsdir=assets[s];color=c=0xE8B64C:s={W}x10:r={FPS}[bar];[s][bar]overlay=x='-w+w*t/{TOT:.2f}':y=0:shortest=1[v]"
run(["ffmpeg","-y","-i","tmp/mudo.mp4","-i",R["voz"],"-i","tmp/wh.wav","-filter_complex",fv+";"+fa,"-map","[v]","-map","[a]","-c:v","libx264","-preset","medium","-crf","20","-maxrate","6000k","-bufsize","12000k","-pix_fmt","yuv420p","-c:a","aac","-b:a","160k","-movflags","+faststart","-t",f"{TOT:.2f}",OUT])
print(OUT,round(TOT,1),"s",round(os.path.getsize(OUT)/1e6,1),"MB",len(partes),"tomas")
