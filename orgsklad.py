# Склад оргтехники
class Sklad:
    contain = {}
    last_id = 0
    data = []

    @staticmethod
    def dep_validate(depart):
        try:
            return bool(str(depart))
        except ValueError:
            return False

    @staticmethod
    def org_validate(org_technic):
        try:
            return isinstance(org_technic, Org)
        except ValueError:
            return False

    @classmethod
    def add_tehnic(cls, org_technic, depart):
        if cls.org_validate(org_technic) and cls.dep_validate(depart):
            print(org_technic.type)
            now_count = cls.contain.get(org_technic.type)
            if not now_count:
                now_count = 0
            cls.contain[org_technic.type] = now_count + 1
            new_row = org_technic.__dict__
            new_row['id'] = cls.last_id = cls.last_id + 1
            new_row['department'] = depart

            cls.data.append(new_row)


class Org:
    def __init__(self, power, color, model):
        self.type = self.__class__.__name__
        self.power = power
        self.color = color
        self.model = model

    def __str__(self):
        dictinary = self.__dict__
        dictinary['class'] = self.__class__.__name__
        return str(self.__dict__)
            # printable_list[param] = self[param]


class Printer(Org):
    def __init__(self, *args, speed):
        Org.__init__(self, *args)
        self.print_speed = speed


class Scanner(Org):
    def __init__(self, *args, speed):
        Org.__init__(self, *args)
        self.scan_speed = speed


class Xerox(Org):
    def __init__(self, *args, speed):
        Org.__init__(self, *args)
        self.copy_speed = speed


org1 = Printer(100, 'green', 'hp-100', speed=100)
print(org1)
Sklad.add_tehnic(org1, 'otdel1')
Sklad.add_tehnic(org1, 'otdel2')
print(Sklad.contain)
print(Sklad.data)
