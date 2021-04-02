# Ищем самую большую цифру в числе
integer = int(input('Введите целое положительное число: '))
maximum = 0
if integer < 0:
    print('число должно быть положительным')
else:
    while(integer > 0) :
        if integer % 10 > maximum:
            maximum = integer % 10
        integer = integer // 10
    print(maximum)
