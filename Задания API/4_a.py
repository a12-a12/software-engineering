from geopy.geocoders import Nominatim


def find_southernmost_city(cities_str):

    geolocator = Nominatim(user_agent="southernmost_city_finder")
    cities = [city.strip() for city in cities_str.split(",")]
    southernmost_city = None
    min_latitude = float('inf')

    for city in cities:
        location = geolocator.geocode(city)
        if location:
            if location.latitude < min_latitude:
                min_latitude = location.latitude
                southernmost_city = city

    return southernmost_city


if __name__ == "__main__":
    cities_str = input("Введите список городов через запятую: ")
    southernmost_city = find_southernmost_city(cities_str)

    if southernmost_city:
        print(f"Самый южный город: {southernmost_city}")
    else:
        print("Города не найдены.")
