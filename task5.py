class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def draw(self):
        Stationery.draw(self)
        print(f'{self.title} рисует круг!')


class Pencil(Stationery):
    def draw(self):
        Stationery.draw(self)
        print(f'{self.title} рисует квадрат!')


class Handle(Stationery):
    def draw(self):
        Stationery.draw(self)
        print(f'{self.title} рисует треугольник!')

pen = Pen('Ручка').draw()
pen = Pencil('Карандаш').draw()
pen = Handle('Маркер').draw()