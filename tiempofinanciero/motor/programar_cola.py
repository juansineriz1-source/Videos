# python3 programar_cola.py [dias_adelante=3]  (desde tiempofinanciero/motor, con BUFFER_API_KEY)
# Buffer gratis: máximo 10 posts programados en total (noticias e historias incluidas).
# Programa los reels "aprobado" de cola-historias.csv a las 10:00 BA, uno por día, hasta N días adelante.
import csv,sys,subprocess,datetime,os,json
D=os.path.dirname(os.path.abspath(__file__)); C=os.path.join(D,'..','cola-historias.csv')
N=int(sys.argv[1]) if len(sys.argv)>1 else 3
rows=list(csv.DictReader(open(C))); hoy=(datetime.datetime.utcnow()-datetime.timedelta(hours=3)).date()
ocupadas={r['fecha'] for r in rows if r['estado']=='programado'}
for r in rows:
    if r['estado']=='programado' and r['fecha'] and datetime.date.fromisoformat(r['fecha'])<hoy: r['estado']='publicado'
for k in range(1,N+1):
    d=(hoy+datetime.timedelta(days=k)).isoformat()
    if d in ocupadas: continue
    r=next((x for x in rows if x['estado']=='aprobado'),None)
    if not r: break
    out=subprocess.run(['python3',os.path.join(D,'publicar_tf.py'),'reel',r['clave_nas'],os.path.join(D,'..',r['caption']),d+'T10:00','500'],capture_output=True,text=True).stdout
    print(r['reel'],d,out.strip()[-160:])
    if 'PostActionSuccess' in out: r['estado']='programado'; r['fecha']=d; ocupadas.add(d)
    else: break
w=csv.DictWriter(open(C,'w',newline=''),fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
