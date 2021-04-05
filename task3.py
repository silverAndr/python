# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.
month = input('Введите месяц - ')
if not month.isdigit() or int(month) <= 0 or int(month) < 1 or int(month) > 12:  # проверяем ввод месяца
    print('Месяц - это положительное целое число, от 1 до 12')
    exit()
month = int(month)
monthes = ['Зима', 'Зима', 'Весна', 'Весна', 'Весна', 'Лето', 'Лето', 'Лето', 'Осень', 'Осень', 'Осень', 'Зима']
print(monthes[month-1])  # через список

dict_seasons = {
    1: 'Весна',
    2: 'Лето',
    3: 'Осень',
    4: 'Зима'
}
dict_monthes = {
    1: {
        'name': 'Январь',
        'season': 4
    },
    2: {
        'name': 'Февраль',
        'season': 4
    },
    3: {
        'name': 'Март',
        'season': 1
    },
    4: {
        'name': 'Апрель',
        'season': 1
    },
    5: {
        'name': 'Май',
        'season': 1
    },
    6: {
        'name': 'Июнь',
        'season': 2
    },
    7: {
        'name': 'Июль',
        'season': 2
    },
    8: {
        'name': 'Август',
        'season': 2
    },
    9: {
        'name': 'Сентябрь',
        'season': 3
    },
    10: {
        'name': 'Октябрь',
        'season': 3
    },
    11: {
        'name': 'Ноябрь',
        'season': 3
    },
    12: {
        'name': 'Декабрь',
        'season': 4
    }
}
dict_month = dict_monthes.get(month)
print('Месяц ' + dict_month['name'] + '. Время года - ' + dict_seasons[dict_month['season']] + '!')  # через словарь
