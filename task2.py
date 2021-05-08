class Road:
    weight = 25  # кг асфальта, для покрытия 1 кв. метра полотна

    def __init__(self, width, length):
        self._width = width
        self._length = length

    def calc(self, weight, depth):
        return self._length * self._width * self.weight * depth

width = 20  # ширина полотна
length = 5000  # длинна дороги в метрах
road_1 = Road(width, length)

depth = 5  # см толщины полотна
print(f'масса асфальта для  покрытия {depth} см полотна, длинной {round(length/1000, 2)} км,'
      f'и шириной {width} м - {round(road_1.calc(25, 5) / 1000, 3)} т.')