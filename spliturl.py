import requests
from requests.exceptions import HTTPError
from requests.exceptions import ConnectionError
import csv as c

er = []
stat = []
red = []
ur = []
finurl = []

def start(url):
    

    try:
        res = requests.get(url, allow_redirects=False)
        

        
        if (res.status_code == 404):
            er.append("404 Error")
            stat.append(res.status_code)
            red.append("-")
        elif (res.status_code == 403):
            er.append("403:Forbidden")
            stat.append(res.status_code)
            red.append("-")
        elif (res.status_code == 302 or res.status_code == 301 or res.status_code == 303):
            if (url.find("https://www.") == 0):
                finurl.append(url[12:])
            elif (url.find("http://www.") == 0):
                finurl.append(url[11:])
            elif (url.find("https://") == 0):
                finurl.append(url[8:])
            elif (url.find("http://") == 0):
                finurl.append(url[7:])

            if (res.headers['Location'].find(finurl[0]) == -1):
                er.append("-")
                stat.append(res.status_code)
                red.append("Redirects to " + str(res.headers['Location']))  
            else:
                er.append("-")
                stat.append(res.status_code)
                red.append("-")
            finurl.clear()
        elif (res.status_code == 200):
            er.append("-")
            stat.append(res.status_code)
            red.append("-")
        else:
            er.append("Unknown Error")
            stat.append(res.status_code)
            red.append("-")

    except HTTPError as err:
        er.append("HTTPError")
        stat.append(res.status_code)
        red.append("-")
    except ConnectionError as e:
        er.append("Site can't be reached.")
        stat.append("000")
        red.append("-")
    except Exception as hm:
        er.append(hm)
        stat.append("-")
        red.append("-")
    except:
        er.append("Unknown Error")
        stat.append(res.status_code)
        red.append("-")



with open('sharewt.csv', newline='', encoding='utf-8') as f:
    er.clear()
    ur.clear()
    stat.clear()
    red.clear()

    reader = c.reader(f)
    print("Running....")
    for i in reader:
        if i[0] != "URLs":
            ur.append(i[0])

    for i in ur:
        start(i)


    
        

with open('sharewt.csv', mode='w') as f:
    head = ['URLs', 'Status', 'Error Message', 'Redirection']
    writer = c.writer(f)

    writer.writerow(head)
    print(len(er))
    for i in range(len(er)):
        writer.writerow([ur[i], stat[i], er[i], red[i]])
    print("Data Updated!")

