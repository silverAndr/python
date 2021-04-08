my_sum = 0

def my_calc(str_numbers):
    my_list = str_numbers.split()
    my_list = list(map(int, my_list))
    return sum(my_list, my_sum)


while True:
    numbers = input('Введите числа через пробел')
    my_sum = my_calc(numbers)
    print(my_sum)

