import random
my_list = [random.randint(0, 100) for _ in range(20)]
with open('nums.txt', 'w') as file:
    if file.write(' '.join(str(x) for x in my_list)):
        print('Записано!')

with open('nums.txt') as file:
    rows = file.readlines()
for numbers in rows:
    nums = [int(el) for el in numbers.split()]
    break
print(f'Сумма {sum(nums)}')
