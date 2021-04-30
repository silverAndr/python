class OwnZeroDivisionError(ZeroDivisionError):
    def __init__(self, txt):
        self.txt = txt

try:
    num1 = int(input('Делимое: '))
    num2 = int(input('Делитель: '))
    if num2 == 0:
        raise OwnZeroDivisionError("Беконечно большое число!")
    res = num1 / num2
except OwnZeroDivisionError as err:
    print(err)
else:
    print(f"Все хорошо. Результат - {res}")
finally:
    print("Программа завершена")
