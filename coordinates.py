from dadata import Dadata
import string

def get_local(latitude, longitude):
    #обращение к api dadata для перевода координат в адрес
    token_dadata = "9b3f375bdd7a7efb457daf31f3a376a23f5bcd50"
    dadata = Dadata(token_dadata)
    result = dadata.geolocate(name="address", lat = latitude, lon = longitude)

    rezul = result[0]; #result - список. resul - словарь

    #замена пробелов на + и добавление города для поискового запроса
    rez = rezul['value'].replace(' ', '+')
    rez = rez.replace('г+Санкт-Петербург,+', '')

    return rez
