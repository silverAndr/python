class ComplexNum:

    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.c = 'a + b * i'

    def __add__(self, other):
        print(f'c1 + c2 = ', end='')
        return f' {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'c1 * c2 = ', end='')
        return f' {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'c = {self.a} + {self.b} * i'


c_1 = ComplexNum(1, -2)
c_2 = ComplexNum(3, 4)

print(c_1)
print(c_2)
print(c_1 + c_2)
print(c_1 * c_2)
