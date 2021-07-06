from bs4 import BeautifulSoup
import requests
import re
import sqlite3

def data_base(user_addres, user_time):
    db = sqlite3.connect('map.db')
    cursor = db.cursor()
    for value in cursor.execute("SELECT * FROM maps"):

        if(_parse(value[0],user_addres ) < user_time):

            return (value)

    return 'У вас слишком мало времени'



def _parse(user_addres,addres):

    url = 'https://www.google.com/search?q=сколько+ехать+от+' + user_addres + '+до+' + addres
    HEADERS = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'
    }

    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')

    try:
        time_drive = soup.find('span', class_='iQIYjb myy6W').get_text(strip=True)
    except:
        try:
            time_drive = soup.find('span', class_='iQIYjb ahzAec').get_text(strip=True)
        except:
            try:
                time_drive = soup.find('span', class_='iQIYjb XKlQuc').get_text(strip=True)
            except:
                print('Error')
    time_drive = [int(s) for s in time_drive.split() if s.isdigit()]

    return(time_drive[0])

