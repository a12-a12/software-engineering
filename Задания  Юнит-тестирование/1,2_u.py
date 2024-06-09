# Задание 1
def test_is_palindrome():
    test_cases = ["radar", "level", "hello", "madam", "noon"]
    for case in test_cases:
        if is_palindrome(case):
            continue
        else:
            print("NO")
            return
    print("YES")

# Задание 2
def is_palindrome(data):
    return data == data[::-1]

input_string = input("Введите строку: ")
if is_palindrome(input_string):
    print("YES")
else:
    print("NO")
