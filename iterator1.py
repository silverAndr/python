# 6.a итератор, генерирующий целые числа, начиная с указанного
from sys import argv
import itertools as itr

start = int(argv[1])

for el in itr.count(start):
    if el > 1000:
        print('стоп машина!')
        break
    else:
        print(el)
