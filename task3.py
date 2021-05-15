class Element:

    def __init__(self, cells):
        if cells <= 0:
            print('кол-во ячеек должно быть положительным числом!')
            return False
        self.cells = cells

    def __add__(self, other):
        return Element(self.cells + other.cells)

    def __sub__(self, other):
        if self.cells > other.cells:
            return Element(self.cells - other.cells)
        print('Недостаточно ячеек для вычитания')
        return False;

    def __mul__(self, other):
        return Element(self.cells * other.cells)

    def __truediv__(self, other):
        if other.cells == 0:
            print('Нельзя делить на пустую клетку')  # скорее всего это условие несработает никогда, потому что другие
            # методы не генерируют пустые клетки, но пусть будет, вдруг измениться что-то в программе
            return False
        return Element(round(self.cells / other.cells, 0))

    def make_order(self, row_len):
        str_cells = ''
        a = 0
        while(a < self.cells):
            str_cells += '*'
            a += 1
            if a % row_len == 0:
                str_cells += '\n'
        return str_cells


element1 = Element(5)
element2 = Element(3)
element3 = element1 + element2
print(element3.make_order(5))