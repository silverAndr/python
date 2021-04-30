import re

class NotIntError(ValueError):
    def __init__(self, txt):
        self.txt = txt


my_list = []

while True:
    num = input('Введите число ("stop" - для выхода): ')
    if num == 'stop':
        break
    if not num:
        print('0')
        num = '0'
    try:
        num_match = re.match(r'(\d*)', num).group()
        if num_match != num:
            raise NotIntError(f"'{num}' - не число.'")
            continue
        my_list.append(int(num))
    except NotIntError as err:
        print(err)

print(my_list)
