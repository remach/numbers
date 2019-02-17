import requests, json, csv
import datetime



f = csv.reader(open("mskCredit.csv", "r",newline='', encoding="utf8"),delimiter=';' )
i=0
payload= []
for row in f:
    payload.append({
        "value": row[4].replace(' ','').replace(',','.'),
    "description_text": row[0],
    "unit": "руб",
    "link": "http://budget.mos.ru/",
    "pub_date": datetime.datetime.now().isoformat()
    }
    )
    i=i+1
    print(i)
    if 20 == i:
        #print(payload)
        i=0
        r = requests.post("http://127.0.0.1:8000/api/number/", json=payload)
        print(r)
        payload= []
        break
    
    
