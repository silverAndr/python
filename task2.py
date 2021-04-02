# Выводим время в формате чч:мм:сс
hours = 0
minutes = 0
sec = int(input('Введите время в секундах - '))
if sec >= 60:
    minutes = sec // 60
    sec = sec % 60
if minutes >= 60:
    hours = minutes // 60
    minutes = minutes % 60
print(f'{hours:02}:{minutes:02}:{sec:02}')
