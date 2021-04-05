# Реализовать структуру данных «Товары».
products = []
product_params = {'name': 'Название', 'price': 'цена', 'count': 'Количество', 'ed': 'ед'}
ind = 0
while True:
    print('Введите товар', str(ind+1))
    current_params = {}
    for param in product_params.keys():
        new_value = input(product_params[param] + ': ')
        if new_value.isdigit() :
            new_value = int(new_value)
        current_params[param] = new_value
    products.append((ind, current_params))
    if input('"0" для завершения ввода: ') == '0':
        break
    ind += 1
print('Вы ввели: ')
print(products)
result = {}
for param in product_params:
    result[param] = set([])
for product in products:
    for param in product_params:
        result[param].add(product[1][param])
for param in product_params:
    result[param] = list(result[param])
print('Аналитика:')
print(result)
