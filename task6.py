def only_nums(string):
    num_list = []
    num = ''
    for char in string:
        if char.isdigit():
            num = num + char
        else:
            if num != '':
                num_list.append(int(num))
                num = ''
    if num != '':
        num_list.append(int(num))
    return sum(num_list)


with open('subjects.txt') as file:
    rows = file.readlines()
new_dict = {}

for row in rows:
    ar_row = row.split(':')
    new_dict[ar_row[0]] = only_nums(ar_row[1])

print(new_dict)
