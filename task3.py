with open('workers.txt') as file:
    rows = file.readlines()
lowers = []
oklads = []
for row in rows:
    name, oklad = row.split()
    oklad = int(oklad)
    oklads.append(oklad)
    if int(oklad) < 20000:
        lowers.append(name)
print('У сотрудников', end=': ')
for lower in lowers:
    print(lower, sep=', ', end=', ')
print('оклад меньше 20000')
avg = sum(oklads)/len(oklads)
print(f'средний оклад {round(avg,2)}')