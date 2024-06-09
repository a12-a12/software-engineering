import folium
from geopy.distance import geodesic

points = [
    (55.7522, 37.6156),  # Красная площадь
    (55.7628, 37.6219),  # Большой театр
    (55.7595, 37.6056),  # Кремль
    (55.7539, 37.5948),  # Храм Христа Спасителя
]

moscow_map = folium.Map(location=points[0], zoom_start=13)

total_distance = 0
for i in range(len(points) - 1):
    total_distance += geodesic(points[i], points[i + 1]).kilometers

middle_point_index = len(points) // 2
middle_point = points[middle_point_index]

for point in points:
    folium.Marker(location=point).add_to(moscow_map)

folium.Marker(
    location=middle_point,
    popup=f"Средняя точка пути<br>Общая длина: {total_distance:.2f} км",
).add_to(moscow_map)

folium.PolyLine(points, color="blue", weight=2.5, opacity=1).add_to(moscow_map)

moscow_map.save("moscow_path_map.html")
