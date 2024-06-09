# Задание 3
def test_is_correct_mobile_phone_number_ru():
    test_cases = ["+79001234567", "89001234567", "+7(900)1234567", "8 (900) 123-45-67", "+7 999 123-45-67", "1234567890"]
    for case in test_cases:
        if is_correct_mobile_phone_number_ru(case):
            continue
        else:
            print("NO")
            return
    print("YES")

# Задание 4
def is_correct_mobile_phone_number_ru(number):
    import re
    pattern = r"(\+7|8)([\s-]?\(?\d{3}\)?[\s-]?\d{3}[\s-]?\d{2}[\s-]?\d{2})"
    return bool(re.match(pattern, number))

input_number = input("Введите номер мобильного телефона: ")
if is_correct_mobile_phone_number_ru(input_number):
    print("YES")
else:
    print("NO")
