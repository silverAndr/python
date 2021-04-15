def to_dict(input_string):
    slovar = {
        "Zero": "Ноль",
        "One": "Один",
        "Two": "Два",
        "Three": "Три",
        "Four": "Четыре",
        "Five": "Пять",
        "Six": "Шесть",
        "Seven": "Семь",
        "Eight": "Восемь",
        "Nine": "Девять"
    }
    one_row = input_string.split(' - ')
    one_row[0] = slovar[one_row[0]]
    return ' - '.join(one_row)

with open('fortask4.txt') as file:
    rows = file.readlines()

rows = list(map(to_dict, rows))
if(rows):
    with open("res-task4.txt", "w") as f_obj:
        print(''.join(rows), file=f_obj)
