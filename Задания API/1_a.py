import folium

stadiums_location = {
    "Лужники": "37.554191,55.715551",
    "Спартак": "37.440262,55.818015",
    "Динамо": "37.559809,55.791540"
}

# Создаем карту Москвы
moscow_map = folium.Map(location=[55.7522, 37.6156], zoom_start=11)

# Добавляем метки стадионов на карту
for stadium, coordinates in stadiums_location.items():
    lon, lat = map(float, coordinates.split(","))  # Исправлено: lon, lat
    folium.Marker([lat, lon], popup=stadium).add_to(moscow_map)

# Сохраняем карту в HTML файл
moscow_map.save("moscow_stadiums_map.html")

# Открываем HTML файл с картой (опционально)
import webbrowser
webbrowser.open("moscow_stadiums_map.html")
