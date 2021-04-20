class Worker:

    def __init__(self, name, surname, position, _income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = _income


class Position(Worker):

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return int(self._income['wage']) + int(self._income['bonus'])


man_1 = Position('Вася', 'Пупкин', 'Бухгалтер', {'wage': 100, 'bonus': 50})
print(f'Сотрудника зовут - {man_1.get_full_name()}!')
print(f'Он получает - {man_1.get_total_income()}тр в месяц')
