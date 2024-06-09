import random
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt
from geopy.geocoders import Nominatim

# Список городов
cities = ["Москва", "Санкт-Петербург", "Новосибирск", "Екатеринбург", "Казань"]


def get_city_coordinates(city_name):
    """Получает координаты города."""
    geolocator = Nominatim(user_agent="city_guesser")
    location = geolocator.geocode(city_name)
    if location:
        return location.latitude, location.longitude
    else:
        return None


def create_city_map(latitude, longitude, zoom=0.5):
    """Создает карту части города."""
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())

    # Устанавливаем область отображения (zoom)
    ax.set_extent([longitude - zoom, longitude + zoom, latitude - zoom, latitude + zoom], crs=ccrs.PlateCarree())

    # Добавляем базовые слои карты
    ax.coastlines(resolution='10m')
    ax.add_feature(cfeature.LAND)
    ax.add_feature(cfeature.OCEAN)
    ax.add_feature(cfeature.RIVERS)
    ax.add_feature(cfeature.LAKES)

    # Добавляем города
    ax.add_feature(
        cfeature.NaturalEarthFeature('cultural', 'populated_places', '10m', edgecolor='black', facecolor='gray'))

    plt.show()


def main():
    """Создает слайд-шоу с картами городов."""
    for city in cities:
        coordinates = get_city_coordinates(city)
        if coordinates:
            lat, lon = coordinates
            create_city_map(lat, lon)
            input("Нажмите Enter для следующего слайда...")


if __name__ == "__main__":
    main()
