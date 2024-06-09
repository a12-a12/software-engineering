import requests
import sys


def get_district(address):
    api_key = 'a6ebce5b-ac41-435c-9d36-b839f96964ef'
    url = 'https://geocode-maps.yandex.ru/1.x/'

    params = {
        'apikey': api_key,
        'format': 'json',
        'geocode': address,
        'kind': 'district'
    }

    response = requests.get(url, params=params)
    data = response.json()

    try:
        district = data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty'][
            'GeocoderMetaData']['Address']['Components'][1]['name']
        return district
    except (IndexError, KeyError):
        return "Район не найден"


if len(sys.argv) != 2:
    print("Пожалуйста, введите адрес в командной строке.")
else:
    address = sys.argv[1]
    district = get_district(address)
    print(f"Район для адреса '{address}': {district}")
