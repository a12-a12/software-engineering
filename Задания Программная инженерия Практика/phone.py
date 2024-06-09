class MyException(Exception):
    def __init__(self, message):
        super().__init__(message)


def phone_number(phone) -> str:
    phone = "".join(phone.split())
    operator = True
    try:
        if not all(phone.split('-')):
            raise MyException('Номер телефона может разделяться только с помощью символа -')
        else:
            phone = phone.replace("-", "")

        if phone.find("+7") != 0 and phone.find("8") != 0:
            # Проверка форматов номеров телефона
            if phone[0] == '+':
                operator = False
                if not any(word in phone for word in ["+359", "+55", "+1", "+7"]):
                    raise MyException("Не удалось определить код страны;")
            else:
                raise MyException('Необходимо чтоб номер телефона начинался с 8 или +7;')

        start_bt = phone.find("(")
        end_bt = phone.find(")")

        if start_bt > -1:
            if end_bt < start_bt or not phone[start_bt + 1:end_bt].isdigit() \
                    or not phone.count("(") == 1 or not phone.count(")") == 1:
                raise MyException('Скобки расположены неверны ')
        else:
            if end_bt > -1:
                raise MyException('Не найден конец одной из скобок.')

        phone = phone.replace('(', "")
        phone = phone.replace(")", "")

        if phone.find("8") == 0:
            phone = "+7" + phone[1:]
        if not phone[1:].isdigit() or not len(phone[1:]) == 11:
            raise MyException(
                'Номер телефона не должен содержать лишние символы')

            # Проверка сотового оператора
        oper = int(phone[2:5])
        if operator == True:
            if oper not in range(910, 940) and oper not in range(980, 990) \
                    and oper not in range(902, 907) and oper not in range(960, 970):
                raise MyException('Оператор сотовой связи не определен')

    except MyException as e:
        print(f"Сообщение об ошибке: {e}")
        return

    return phone


print(phone_number(input('Введите номер телефона:')))