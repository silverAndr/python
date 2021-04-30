from datetime import datetime

class Date:

    def __init__(self, date):
        if not Date.validate(date):
            print("Неверный формат даты, должен быть 'день-месяц-год'")
            exit(0)
        self.date = date
        print('объект создан')

    @classmethod
    def to_int(cls, date):
        if cls.validate(date):
            return list(map(int, date.split('-')))
        else:
            print("Неверный формат даты, должен быть 'день-месяц-год'")
            exit(0)

    @staticmethod
    def validate(date):
        try:
            return bool(datetime.strptime(date, '%d-%m-%Y'))
        except ValueError:
            return False


# new_day = Date('31-05-2021')
day, month, year = Date.to_int('32-05-2021')
print(day, type(day))
print(month, type(month))
print(year, type(year))
