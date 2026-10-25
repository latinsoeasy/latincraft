# Erzeugt vocab.json aus der Klett-PDF (arabische Spalte wird bewusst weggelassen)
import pdfplumber, json, re, sys
src = sys.argv[1] if len(sys.argv)>1 else 'pon_ges_ve_bev_arabisch.pdf'
rows=[]; lek='Salve!'
with pdfplumber.open(src) as pdf:
    for p in pdf.pages:
        for t in p.extract_tables():
            for r in t:
                if not r or r[0]=='Lektion' : continue
                c=[(x or '').replace('\n',' ').strip() for x in r]
                if len(c)<5: continue
                if c[0]: lek=c[0]
                rows.append((lek,c[1],c[2] if len(c)>5 else '',c[-3] if len(c)>5 else c[2],c[-2]))
out={}; order=[]
def lkey(l):
    m=re.search(r'\d+',l); return int(m.group()) if m else 0
for lek,la,extra,de,en in rows:
    if not la or not de: continue
    k=(lkey(lek),la)
    if k not in out:
        out[k]={'l':lkey(lek),'la':la,'de':[],'en':[]}; order.append(k)
    for lst,v in ((out[k]['de'],de),(out[k]['en'],en)):
        if v and v not in lst: lst.append(v)
data=[dict(id=i,l=out[k]['l'],la=out[k]['la'],de=' | '.join(out[k]['de']),en=' | '.join(out[k]['en'])) for i,k in enumerate(order)]
json.dump(data,open('vocab.json','w',encoding='utf-8'),ensure_ascii=False,separators=(',',':'))
from collections import Counter
print(len(data)); print(sorted(Counter(d['l'] for d in data).items()))
