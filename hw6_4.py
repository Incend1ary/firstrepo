class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        print(f"Машина {self.name} создана")

    def go(self):
        print(f"{self.name} поехала")

    def stop(self):
        print(f"{self.name} остановилась")

    def turn(self, side):
        print(f"{self.name} развернулась {side}")

    def show_speed(self):
        print(f"{self.name}: скорость автомобиля {self.speed}")


class TownCar(Car):
    def show_speed(self):
        print(f'{self.name}: скорость автомобиля {self.speed} превышение скорости'
              if self.speed > 60 else f"{self.name}: скорость автомобиля {self.speed}")


class SportCar(Car):
    '''спорт'''


class WorkCar(Car):
    def show_speed(self):
        print(f'{self.name}: скорость автомобиля {self.speed} превышение скорости'
              if self.speed > 40 else f"{self.name}: скорость автомобиля {self.speed}")


class PoliceCar(Car):
    '''полиция'''
    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)


car1 = TownCar(65, "red", "Lexus")
car1.go()
car1.show_speed()
car1.turn("вправо")
car1.stop()


car2 = PoliceCar(80, "blue", "Infinity")
car2.go()
car2.show_speed()
car2.stop()