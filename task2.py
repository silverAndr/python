# функция, принимающая несколько параметров, описывающих данные пользователя

def user_data(name, s_name, b_year, city, email, phone):
    print(f'Имя: {name}, фамилия: {s_name}, год рождения: {b_year}, город проживания: {city}, email: {email},' \
           f' телефон: {phone}')

while True:
    print('Введите данные пользователя: ')
    user_data(
        name=input('Имя: '),
        city=input('город проживания: '),
        email=input('email: '),
        phone=input('телефон: '),
        s_name=input('фамилия: '),
        b_year=input('год рождения: ')
    )
