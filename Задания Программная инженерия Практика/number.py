from collections import deque


def poland_number():
    input_str = str(input('Введите выражение:'))
    stack = deque()
    i = -1
    while i < len(input_str) - 1:
        i += 1
        symbol = input_str[i]
        if symbol == ' ':
            continue
        elif symbol not in ('/', '*', '+', '-'):
            i += 1
            while input_str[i] != ' ':
                i_str = symbol + input_str[i]
                i += 1
            stack.append(symbol)
        else:
            a = stack.pop()
            b = stack.pop()
            result = eval(f'{b}{symbol}{a}')
            print(f'{b}{symbol}{a}')
            stack.append(result)
    return stack[0]

print(poland_number())