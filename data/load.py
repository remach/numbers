import requests, json, csv
import datetime



f = csv.reader(open("mskCredit.csv", "r",newline='', encoding="utf8"),delimiter=';' )
for row in f:
    payload= {
        "value": row[4].replace(' ','').replace(',','.'),
    "description_text": row[0],
    "unit": "руб",
    "link": "http://budget.mos.ru/",
    "pub_date": datetime.datetime.now()
    }
    r = requests.put("http://127.0.0.1:8000/number/", data=payload)
    print(row[4])
    