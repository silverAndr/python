import time

class TrafficLight:
    def running(self):
        while True:
            self.__color = 'красный'
            self.status()
            time.sleep(7)
            self.__color = 'желтый'
            self.status()
            time.sleep(2)
            self.__color = 'зеленый'
            self.status()
            time.sleep(10)

    def status(self):
        print(f'Сейчас горит {self.__color}')

traffic_light = TrafficLight()
traffic_light.running()
