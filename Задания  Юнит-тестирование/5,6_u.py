import re

def strip_punctuation_ru(data):

  return re.sub(r'[^\w\s]', '', data).strip()
  # Задание 5
def test_strip_punctuation_ru():
  """Тестирующая программа для функции strip_punctuation_ru."""
  tests = [
    ("Привет, мир!", "Привет мир"),
    ("Как дела?  Хорошо.", "Как дела Хорошо"),
    ("Сегодня,  завтра,  послезавтра.", "Сегодня завтра послезавтра"),
    ("123.456,789", "123 456 789"),
  ]
  passed = True
  for data, expected in tests:
    result = strip_punctuation_ru(data)
    if result != expected:
      print(f"Тест для '{data}'. Ожидается: '{expected}', Получено: '{result}'")
      passed = False
  if passed:
    print("YES")
  else:
    print("NO")

if __name__ == "__main__":

  test_strip_punctuation_ru()

  # Задание 6
  data = input("Введите текст: ")
  result = strip_punctuation_ru(data)
  print(f"Текст без знаков препинания: {result}")
