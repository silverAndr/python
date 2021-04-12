# 6.b итератор, повторяющий элементы некоторого списка, определенного заранее
import itertools as itr

my_list = [2, 65, 3, 5, 8, 14, 28, 38, 53, 46, 31, 2, 4]

с = 0
for el in itr.cycle(my_list):
    if с > 100:
        print('Стоп машина!')
        break
    print(el)
    с += 1
