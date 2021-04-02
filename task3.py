# Ищем сумму чисел n + nn + nnn
num = input('введите целое число - ')
num1 = int(num)
num2 = int(num * 2)
num3 = int(num * 3)
result = num1 + num2 + num3
print(num1, num2, num3, sep=' + ', end=f' = {result}')
