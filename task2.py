with open('data.txt') as file:
    rows = file.readlines()
print(f'Всего {len(rows)} строк')
i = 0
for string in rows:
    words = string.split()
    i += 1
    print(f'в {i} строке количество строк = {len(words)} ')
