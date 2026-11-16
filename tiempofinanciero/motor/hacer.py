# Arma el spec de un reel de historia desde una receta corta r/tfNN.py y el guion.
# python3 hacer.py NN  -> tf-NN.json (después: python3 armar_tf3.py tf-NN.json reel-tfNN-tema.mp4)
import sys,re,json,glob,os,subprocess
from banco import cargar
NN=sys.argv[1]; I=cargar()
G=glob.glob(f'/home/user/videos/tiempofinanciero/guiones/tf-{NN}-*.md')[0]
rows=[l.split('|')[2].strip() for l in open(G) if re.match(r'\|\s*\d+\s*\|',l)]
def crop(info):
    t=(info['txt']+' '+info['nota']).lower(); w,h=map(int,info['res'].split('x'))
    if 'costados' in t or ('franjas' in t and 'arriba' not in t and w/h>1.5): return f"{round(h*4/3)}:{h}:{round((w-h*4/3)/2)}:0"
    if 'arriba y abajo' in t: return f"{w}:{round(w*9/16)}:0:{round((h-w*9/16)/2)}"
    return None
def A(ref,k,h,pie=None,cred=None,w=1,**kw):
    c,_,ss=ref.partition('@'); ss=ss or '0.5'
    if c.isdigit():
        if not os.path.exists(f'clips/{c}.mp4'): subprocess.run(['python3','clip.py','bajar',c],check=True,capture_output=True)
        d=dict(g='archivo',bg=f'c:{c}@{ss}',k=k,h=h,cred=cred or 'Video: Pixabay')
    else:
        i=I[c]; d=dict(g='archivo',bg=f"v:{i['path']}@{ss}",k=k,h=h,cred=cred or ('Video: '+i['canal'] if i['canal'].startswith('Pixabay') else 'Archivo · '+i['canal']))
        cr=crop(i)
        if cr: d['crop']=cr
    if pie: d['pie']=pie
    d.update(kw); return ['g',w,d]
def N(num,k,h=None,sub=None,src=None,color='bl',row=None,w=1,**kw):
    d=dict(g='num',k=k,num=num,color=color,en=0.1); 
    for a,b in (('h',h),('sub',sub),('src',src),('row',row)):
        if b: d[a]=b
    d.update(kw); return ['g',w,d]
def T(k,h,sub=None,bg=None,w=1,size=150,**kw):
    d=dict(g='titulo',k=k,h=h,size=size,en=0.1)
    if sub: d['sub']=sub
    if bg: d['bg']=bg if bg.startswith(('c:','v:')) else f"v:{I[bg.split('@')[0]]['path']}@{bg.partition('@')[2] or '0.5'}"
    d.update(kw); return ['g',w,d]
def B(k,h,bars,src=None,w=1,**kw):
    n=len(bars); d=dict(g='barras',k=k,h=h,bars=[dict(label=l,v=v,txt=t,color=c,en=round(0.15+0.5*i/max(1,n-1),2)) for i,(l,v,t,c) in enumerate([(b+('gr',))[:4] if len(b)==3 else b for b in bars])])
    if src: d['src']=src
    d.update(kw); return ['g',w,d]
def L(k,h,pts,xl=None,src=None,label='',color='roj',w=1,**kw):
    d=dict(g='linea',k=k,h=h,series=[dict(pts=pts,label=label,color=color,fmt=False)])
    if xl: d['xl']=xl
    if src: d['src']=src
    d.update(kw); return ['g',w,d]
def F(k,h,items,w=1,**kw):
    n=len(items); d=dict(g='flujo',k=k,h=h,items=[dict(t=t,en=round(0.1+0.7*i/max(1,n-1),2)) for i,t in enumerate(items)]); d.update(kw); return ['g',w,d]
def Li(k,h,items,w=1,**kw):
    n=len(items); its=[]
    for i,t in enumerate(items):
        e=dict(t=t[0],en=round(0.15+0.6*i/max(1,n-1),2))
        if len(t)>1 and t[1]: e['r']=t[1]
        if len(t)>2: e['hi']=True
        its.append(e)
    d=dict(g='lista',k=k,h=h,items=its); d.update(kw); return ['g',w,d]
def S(k,h,items,src=None,w=1,**kw):
    n=len(items); d=dict(g='sello',k=k,h=h,items=[dict(t=t,st=st,en=round(0.15+0.6*i/max(1,n-1),2)) for i,(t,st) in enumerate(items)])
    if src: d['src']=src
    d.update(kw); return ['g',w,d]
def Q(texto,autor=None,k=None,w=1):
    d=dict(g='cita',texto=texto,en=0.3)
    if autor: d['autor']=autor
    if k: d['k']=k
    return ['g',w,d]
def R(big,color='roj',w=1): return ['g',w,dict(g='remate',big=big,color=color,en=0.15)]
env=dict(A=A,N=N,T=T,B=B,L=L,F=F,Li=Li,S=S,Q=Q,R=R)
exec(open(f'r/tf{NN}.py').read(),env)
segs=env['SEGS']; assert len(segs)==len(rows),(len(segs),len(rows))
P=env['PORTADA']
ref,_,ss=P['img'].partition('@'); ref=ref.replace('c:','',1) if ref.startswith('c:') and ref[2:].isdigit() else ref
if ref in I or ref.isdigit():
    if ref.isdigit() and not os.path.exists(f'clips/{ref}.mp4'): subprocess.run(['python3','clip.py','bajar',ref],check=True,capture_output=True)
    out=f"img/fr-{ref.replace(':','-')}.jpg"; src=f'clips/{ref}.mp4' if ref.isdigit() else I[ref]['path']
    subprocess.run(['ffmpeg','-v','error','-y','-ss',ss or '1','-i',src,'-frames:v','1',out],check=True); P['img']=out
spec=dict(voz=f'voz-tf{NN}.wav',palabras=env.get('PALABRAS',f'voz-tf{NN}.json'),tempo=1.21,cierre=1.8,
  portada=dict(g='portada',pos=P.get('pos','50% 50%'),k=P.get('k','HISTORIAS DE LA BOLSA'),**{k:v for k,v in P.items() if k not in('pos','k')}),
  segs=[dict(txt=t,vis=v) for t,v in zip(rows,segs)])
json.dump(spec,open(f'tf-{NN}.json','w'),ensure_ascii=False,indent=1); print('ok',f'tf-{NN}.json',len(rows),'filas')
