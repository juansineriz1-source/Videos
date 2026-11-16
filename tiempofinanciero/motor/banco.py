# Banco de recortes: índice unificado. Uso: python3 banco.py palabra [palabra...]  (AND, sin tildes)
import csv,sys,unicodedata,os,json
B='banco'
def norm(s): return ''.join(c for c in unicodedata.normalize('NFD',s.lower()) if unicodedata.category(c)!='Mn')
def cargar():
    out={}
    for f in (f'{B}/indice.csv',f'{B}/extra/indice-extra.csv',f'{B}/indice-px.csv'):
        for r in csv.DictReader(open(f,encoding='utf-8-sig')):
            a=r['archivo']; p=f"{B}/{r['carpeta']}/{a}"
            if not os.path.exists(p): continue
            ab=''.join(x[0] for x in r['carpeta'].split('-')) if r['carpeta']!='extra' else ''; key=(ab+':' if ab else '')+a[:-4]
            out[key]=dict(path=p,ve=r['que_se_ve'],txt=r['tiene_texto_o_logo'],res=r['resolucion'],canal=r['canal'],nota=r.get('nota',''),cat=r['categoria'],dur=r['duracion_s'],titulo=r.get('programa_titulo',''),fecha=r.get('fecha_programa',''))
    return out
if __name__=='__main__':
    I=cargar(); q=[norm(x) for x in sys.argv[1:]]
    for k,v in I.items():
        h=norm(' '.join([v['ve'],v['cat'],v['nota'],v['titulo']]))
        if all(x in h for x in q): print(k,v['res'],v['dur']+'s','|',v['ve'][:110],'|',v['txt'][:40],'|',v['canal'])
