# функция, принимающаю два числа (позиционные аргументы) и выполняющую их деление
def my_del(num1, num2):
    if num2 == '0':
        error = 'Нельзя делить на 0!'
        return 'Ошибка: ' + error
    return float(num1) / float(num2)


while True:
    a = input('Введите делимое: ')
    b = input('Введите делитель: ')
    print(my_del(a, b))
