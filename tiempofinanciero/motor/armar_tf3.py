# Armador v3 de reels @tiempofinancierok (gráficos g3.html, material real, música).  python3 armar_tf3.py <reel.json> <salida.mp4>
# vis: ["c:ID@ss",peso] clip Pixabay | ["v:footage/x.mp4@ss",peso,{"cred":"AP Archive","pos":0.5}] material real |
#      ["g",peso,{...}] gráfico; si lleva "bg":"c:ID@ss" o "v:ruta@ss" se dibuja encima del video
import json,sys,os,re,subprocess
R=json.load(open(sys.argv[1])); OUT=sys.argv[2]; W,H,FPS=1080,1920,30; T=R.get("tempo",1.0)
os.makedirs("tmp",exist_ok=True)
def run(a):
    r=subprocess.run(a,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
    if r.returncode: sys.exit("ERROR "+" ".join(a[:6])+"\n"+r.stderr.decode()[-800:])
def src(v):
    c,_,ss=v[2:].partition("@"); return (f"clips/{c}.mp4" if v.startswith("c:") else c), (ss or "0.5")
pal=[[w["start_time"]/T,w["end_time"]/T,w["text"]] for w in json.load(open(R["palabras"]))["original_words"]]
DUR=float(subprocess.check_output(["ffprobe","-v","0","-show_entries","format=duration","-of","csv=p=0",R["voz"]]))/T
tok=lambda t: re.sub(r"[^\wáéíóúñü]","",t.lower())
ini=[0]
for s in R["segs"]: ini.append(ini[-1]+len(s["txt"].split()))
if ini[-1]!=len(pal):
    L=lambda t: len(re.sub(r"\W","",t)); tot=sum(L(s["txt"]) for s in R["segs"]); cum=[0]
    for p in pal: cum.append(cum[-1]+L(p[2]))
    acc=0; ini=[0]
    for s in R["segs"]: acc+=L(s["txt"]); ini.append(min(range(len(pal)+1),key=lambda j:abs(cum[j]/cum[-1]-acc/tot)))
    ini[-1]=len(pal); print("AVISO: palabras no coinciden, alineado por letras")
cortes=[0.0]+[pal[j][0]-0.06 for j in ini[1:-1]]+[DUR+0.25]
partes=[];cuts=[];k=0;largas=[]
for i,s in enumerate(R["segs"]):
    a,b=cortes[i],cortes[i+1]; tw=sum(v[1] for v in s["vis"]); t0=a
    for v in s["vis"]:
        vis,peso=v[0],v[1]; d=(b-a)*peso/tw; p=f"tmp/p{k}.mp4"; k+=1; cuts.append(t0)
        if d>5.6: largas.append((i+1,round(d,1)))
        if vis=="g":
            at={}
            for j in range(ini[i],ini[i+1]): at.setdefault(tok(pal[j][2]),max(0,pal[j][0]-t0))
            g=v[2]; cfg=json.dumps({"p":g,"d":d,"at":at,"t0":t0},ensure_ascii=False)
            run(["node","render3.js",p,f"{d:.3f}",cfg]+(list(src(g["bg"])) if g.get("bg") else []))
        else:
            c,ss=src(vis); o=v[2] if len(v)>2 else {}; z=f"(1+0.05*t/{d:.3f})"; fx=o.get("pos",0.5)
            cred=o.get("cred"); dt=(f",drawtext=fontfile=assets/Montserrat-SemiBold.ttf:text='{cred}':x=40:y=250:fontsize=26:fontcolor=white@0.85:box=1:boxcolor=black@0.45:boxborderw=10" if cred else "")
            look="eq=contrast=1.06:saturation=0.9:brightness=-0.02,vignette=PI/5"
            run(["ffmpeg","-y","-stream_loop","-1","-ss",ss,"-i",c,"-vf",
              f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H}:(iw-ow)*{fx}:(ih-oh)/2,setsar=1,fps={FPS},scale=w='trunc({W}*{z}/2)*2':h=-2:eval=frame,crop={W}:{H},{look}{dt}",
              "-t",f"{d:.3f}","-an","-c:v","libx264","-preset","veryfast","-crf","16","-pix_fmt","yuv420p",p])
        partes.append(p); t0+=d
if R.get("portada"):
    run(["node","render3.js",OUT.replace(".mp4","-portada.png"),"3",json.dumps({"p":R["portada"],"d":3,"at":{}},ensure_ascii=False)])
if R.get("cierre"):
    p=f"tmp/p{k}.mp4"; run(["node","render3.js",p,str(R["cierre"]),json.dumps({"p":{"g":"cierre"},"d":R["cierre"],"at":{},"t0":cortes[-1]})]); partes.append(p); cuts.append(cortes[-1])
TOT=cortes[-1]+R.get("cierre",0)
open("tmp/l.txt","w").write("".join(f"file '{os.path.abspath(p)}'\n" for p in partes))
run(["ffmpeg","-y","-f","concat","-safe","0","-i","tmp/l.txt","-c","copy","tmp/mudo.mp4"])
def tc(x): x=max(0,x); return f"{int(x//3600)}:{int(x%3600//60):02d}:{x%60:05.2f}"
ass=["[Script Info]","ScriptType: v4.00+","PlayResX: 1080","PlayResY: 1920","WrapStyle: 0","","[V4+ Styles]",
"Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding",
"Style: Cap,Montserrat Black,80,&H00FFFFFF,&H00FFFFFF,&H001A0D07,&HB4000000,0,0,0,0,100,100,1,0,1,8,5,2,70,70,340,1",
"","[Events]","Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text"]
for i,s in enumerate(R["segs"]):
    g=[]
    def volcar(g,fin):
        for m,(a,b,w) in enumerate(g):
            e=g[m+1][0] if m+1<len(g) else min(b+0.25,fin)
            txt=" ".join(((r"{\c&H4BB8F2&\fscx114\fscy114}"+x[2]+r"{\c&HFFFFFF&\fscx100\fscy100}") if n==m else x[2]) for n,x in enumerate(g)).upper()
            ass.append(f"Dialogue: 0,{tc(a)},{tc(e)},Cap,,0,0,0,,"+(r"{\fad(40,0)\fscx90\fscy90\t(0,90,\fscx100\fscy100)}" if m==0 else "")+txt)
    for j in range(ini[i],ini[i+1]):
        g.append(pal[j])
        if len(g)>=3 or sum(len(x[2]) for x in g)>=13 or pal[j][2][-1] in ".?!:":
            volcar(g,pal[j+1][0] if j+1<len(pal) else DUR+0.2); g=[]
    if g: volcar(g,cortes[i+1])
open("tmp/s.ass","w").write("\n".join(ass)+"\n")
cs=cuts[1:]; n=len(cs)
run(["ffmpeg","-y","-f","lavfi","-i","anoisesrc=d=0.4:c=pink:a=0.6","-af","highpass=f=500,lowpass=f=4500,afade=t=in:d=0.16,afade=t=out:st=0.16:d=0.24,volume=0.20","tmp/wh.wav"])
mus=R.get("musica"); ins=["-i","tmp/mudo.mp4","-i",R["voz"],"-i","tmp/wh.wav"]+(["-stream_loop","-1","-i",mus] if mus else [])
fa=f"[1:a]atempo={T},loudnorm=I=-15:TP=-1.5,apad=pad_dur={R.get('cierre',0)+0.5}[vz];[2:a]asplit={n}"+"".join(f"[w{q}]" for q in range(n))+";"+"".join(f"[w{q}]adelay={int(max(0,c-0.17)*1000)}:all=1[d{q}];" for q,c in enumerate(cs))
if mus: fa+=f"[3:a]volume={R.get('musica_vol',0.11)},afade=t=in:d=1.2,afade=t=out:st={TOT-1.5:.2f}:d=1.5[mu];"
fa+="[vz]"+"".join(f"[d{q}]" for q in range(n))+("[mu]" if mus else "")+f"amix=inputs={n+1+(1 if mus else 0)}:normalize=0:duration=first[a]"
fv=f"[0:v]ass=tmp/s.ass:fontsdir=assets[s];color=c=0xF2B84B:s={W}x10:r={FPS}[bar];[s][bar]overlay=x='-w+w*t/{TOT:.2f}':y=0:shortest=1[v]"
run(["ffmpeg","-y",*ins,"-filter_complex",fv+";"+fa,"-map","[v]","-map","[a]","-c:v","libx264","-preset","medium","-crf","20","-maxrate","6500k","-bufsize","13000k","-pix_fmt","yuv420p","-c:a","aac","-b:a","160k","-movflags","+faststart","-t",f"{TOT:.2f}",OUT])
print(OUT,round(TOT,1),"s",round(os.path.getsize(OUT)/1e6,1),"MB",len(partes),"tomas","| tomas largas (seg,dur):",largas)
