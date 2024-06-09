import math

# Определяем функцию, считающую расстояние между двумя точками, заданными координатами
def lonlat_distance(a, b):

    degree_to_meters_factor = 111 * 1000  # 111 километров в метрах
    a_lon, a_lat = a
    b_lon, b_lat = b

    # Берем среднюю по широте точку и считаем коэффициент для нее.
    radians_lattitude = math.radians((a_lat + b_lat) / 2.)
    lat_lon_factor = math.cos(radians_lattitude)

    # Вычисляем смещения в метрах по вертикали и горизонтали.
    dx = abs(a_lon - b_lon) * degree_to_meters_factor * lat_lon_factor
    dy = abs(a_lat - b_lat) * degree_to_meters_factor

    # Вычисляем расстояние между точками.
    distance = math.sqrt(dx * dx + dy * dy)

    return distance


def main():
    # Ввод адресов пользователем
    home_address = input("Введите адрес вашего дома (долгота, широта через запятую): ")
    university_address = input("Введите адрес университета (долгота, широта через запятую): ")

    # Преобразование адресов в координаты
    try:
        home_lon, home_lat = map(float, home_address.split(","))
        university_lon, university_lat = map(float, university_address.split(","))
    except ValueError:
        print("Ошибка: Некорректный формат координат. Вводите долготу и широту через запятую.")
        return

    # Вычисление расстояния
    distance = lonlat_distance((home_lon, home_lat), (university_lon, university_lat))

    # Вывод результата
    print(f"Расстояние от вашего дома до университета: {distance:.2f} метров")


if __name__ == "__main__":
    main()
