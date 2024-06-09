import requests
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

def find_nearest_pharmacy(address):

  # Преобразование адреса в координаты
  geolocator = Nominatim(user_agent="pharmacy_finder")
  location = geolocator.geocode(address)
  if not location:
    print("Адрес не найден.")
    return None

  # Запрос к OpenStreetMap API для поиска аптек
  overpass_url = "https://overpass-api.de/api/interpreter"
  overpass_query = f"""
  [out:json];
  (
    node["amenity"="pharmacy"](around:5000, {location.latitude}, {location.longitude});
  );
  out;
  """

  response = requests.get(overpass_url, params={'data': overpass_query})
  data = response.json()

  # Поиск ближайшей аптеки
  nearest_pharmacy = None
  min_distance = float('inf')
  for element in data["elements"]:
    if "tags" in element and "name" in element["tags"]:
      pharmacy_location = (element["lat"], element["lon"])
      distance = geodesic(location.point, pharmacy_location).kilometers
      if distance < min_distance:
        min_distance = distance
        nearest_pharmacy = {
            "name": element["tags"]["name"],
            "address": element["tags"].get("addr:street", "") + ", " + element["tags"].get("addr:housenumber", ""),
            "distance": distance
        }

  return nearest_pharmacy

if __name__ == "__main__":
  user_address = input("Введите адрес: ")
  nearest_pharmacy = find_nearest_pharmacy(user_address)

  if nearest_pharmacy:
    print(f"Ближайшая аптека:\n"
          f"Название: {nearest_pharmacy['name']}\n"
          f"Адрес: {nearest_pharmacy['address']}\n"
          f"Расстояние: {nearest_pharmacy['distance']:.2f} км")
  else:
    print("Аптеки не найдены.")
