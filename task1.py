print('Запиши строки в файл, используй пробел для выхода:')
my_rows = []
while True:
    new_row = input()
    if new_row == ' ':
        file = open('data.txt', 'w')
        file.writelines(my_rows)
        file.close()
        print('Я все записал!')
        break
    my_rows.append(new_row+'\n')

