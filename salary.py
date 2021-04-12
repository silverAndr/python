# task 1
from sys import argv
script_name, production, rate, prize = argv

salary = int(production) * int(rate) + int(prize)
print(salary)
