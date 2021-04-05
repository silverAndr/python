# Для списка реализовать обмен значений соседних элементов
list_length = input('Введите длинну списка - ')
if not list_length.isdigit() or int(list_length) <= 0:  # проверяем ввод длины списка
    print('Длинна - это положительное, целое число')
    exit()
list_length = int(list_length)
ind = 0
list = []
while ind < list_length:
    list.insert(ind, input('Введите элемент ' + str(ind) + ' - '))
    ind += 1
print(list)  # выводим введенный список
index = 0
for item in list:
    if index % 2 == 1:
        list[index], list[index-1] = list[index-1], list[index]
    index += 1
print(list)  # выводим измененный список
