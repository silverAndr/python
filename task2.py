from abc import ABC, abstractmethod

class Clothes(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def material_count(self):
        pass

    def __str__(self):
        return f'Общий расход по {self.name} = {self.material_count}'


class Palto(Clothes):

    def __init__(self, name, v):
        Clothes.__init__(self, name)
        self.v = v

    @property
    def material_count(self):
        return self.v / 6.5 + 0.5


class Costum(Clothes):

    def __init__(self, name, h):
        Clothes.__init__(self, name)
        self.h = h

    @property
    def material_count(self):
        return 2 * self.h + 0.3


clother_1 = Palto('Пальто', 48)
clother_2 = Costum('Костюм', 175)

sum_materil = clother_1.material_count + clother_2.material_count
print(sum_materil)