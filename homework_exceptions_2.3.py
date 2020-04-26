"""Польская нотация для двух положительных чисел"""

print('Доступные операции для двух положительных чисел: \nСложение \nВычитание \nУмножение \nДеление\n ')

def main():

    inp = input('Введите знак операции и два числа. Разделяйте каждый элемент пробелом \n ')
    inp = inp.split(' ')

    inp_string = list(filter(None, inp))

    action = 0

    try:
        assert inp_string[0] in ['+', '-', '*', '/']
    except AssertionError:
        print('\n Ваша операция не находится в списке допустимых')
    try:
        if int(inp_string[1]) < 0 or int(inp_string[2]) < 0:
            print('Вы ввели отрицательное число')
            main()
        if not isinstance(inp_string[1:2], int):
            a = int(inp_string[1])
            b = int(inp_string[2])
            c = a / b        
    except ZeroDivisionError:
        print('\n Вы пытаетесь поделить на ноль')
    except ValueError:
        print('\n Вы ввели не числовые значения')
    except IndexError:
        print('\n Вы ввели не достаточно аргументов')
    if len(inp_string) > 3:
        print('\n Вы ввели избыточное количество аргументов')

    for i in inp_string:
        if i == '-':
            action = int(inp_string[1]) - int(inp_string[2])
            print(f'\n Результат равен {action}')
            break
        elif i == '+':
            action = int(inp_string[1]) + int(inp_string[2])
            print(f'\n Результат равен {action}')
            break
        elif i == '*':
            action = int(inp_string[1]) * int(inp_string[2])
            print(f'\n Результат равен {action}')
            break
        elif i == '/':
            action = int(inp_string[1]) / int(inp_string[2])
            print(f'\n Результат равен {action}')
            break
    
main()