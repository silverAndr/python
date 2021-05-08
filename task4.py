class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def tern(self, direction):
        print(f'Машина повернула {direction}')

    def show_speed(self):
        print(self.speed)


class TownCar(Car):

    def show_speed(self):
        if (int(self.speed) > 60):
            print('Превышена скорость!')
        Car.show_speed(self)


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if (int(self.speed) > 60):
            print('Превышена скорость!')
        Car.show_speed(self)


class PoliceCar(Car):

    def __init__(self, *args):
        Car.__init__(self, *args)
        self.is_police = True


car1 = TownCar(35, 'red', 'lada', False)
car1.go()
car1.show_speed()
car2 = TownCar(75, 'white', 'kia', False)
car2.show_speed()
car3 = WorkCar(35, 'black', 'maz', False)
car3.show_speed()
car4 = SportCar(135, 'red', 'ferarry', False)
car4.show_speed()
car5 = PoliceCar(125, 'blue', 'policy', True)
car5.show_speed()
