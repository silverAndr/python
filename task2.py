my_list = [2, 65, 3, 5, 8, 14, 28, 38, 53, 46, 31, 2, 4]
print('имходный список:', my_list)
new_list = [el for i, el in enumerate(my_list) if my_list[i] > my_list[i-1]]
print('Сгенерированный список:', new_list)
