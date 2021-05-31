from bs4 import BeautifulSoup
import requests
import re
import sqlite3

def parse():

    url = 'https://www.google.com/search?q=сколько+ехать+от+московский+проспект+207+до+сенная+площадь'
    HEADERS = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'
    }

    response = requests.get(url, headers = HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    #time_drive = ''
    try:
        time_drive = soup.find('span', class_ = 'iQIYjb myy6W').get_text(strip = True)
    except:
        try:
            time_drive = soup.find('span', class_='iQIYjb ahzAec').get_text(strip=True)
        except:
            try:
                time_drive = soup.find('span', class_='iQIYjb XKlQuc').get_text(strip=True)
            except:
                pass
    time_drive = [int(s) for s in time_drive.split() if s.isdigit()]
    #iQIYjb ahzAec iQIYjb XKlQuc
    print(time_drive)

parse()