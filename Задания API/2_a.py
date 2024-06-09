import folium
from geopy.distance import geodesic

# Определите список координат точек
points = [
    (55.7522, 37.6156),  # Красная площадь
    (55.7628, 37.6219),  # Большой театр
    (55.7595, 37.6056),  # Кремль
    (55.7539, 37.5948),  # Храм Христа Спасителя
]

# Создайте карту Москвы
moscow_map = folium.Map(location=points[0], zoom_start=13)

# Вычислите длину пути
total_distance = 0
for i in range(len(points) - 1):
    total_distance += geodesic(points[i], points[i + 1]).kilometers

# Найдите среднюю точку пути
middle_point_index = len(points) // 2
middle_point = points[middle_point_index]

# Добавьте метки точек на карту
for point in points:
    folium.Marker(location=point).add_to(moscow_map)

# Добавьте метку средней точки с информацией о расстоянии
folium.Marker(
    location=middle_point,
    popup=f"Средняя точка пути<br>Общая длина: {total_distance:.2f} км",
).add_to(moscow_map)

# Нарисуйте линии, соединяющие точки
folium.PolyLine(points, color="blue", weight=2.5, opacity=1).add_to(moscow_map)

# Сохраните карту в HTML файл
moscow_map.save("moscow_path_map.html")
