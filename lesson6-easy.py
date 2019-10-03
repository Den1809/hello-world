# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

class TownCar:
    def __init__(self):
        self.speed = 60
        self.color = 'white'
        self.name = 'TownCar'
        self.is_police = False
        self.go()

    def go(self):
        print(self.name, 'go')

    def stop(self):
        print(self.name, 'stop')

    def turn(self, direction):
        print(self.name, 'turn', direction)


class SportCar:
    def __init__(self):
        self.speed = 100
        self.color = 'red'
        self.name = 'SportCar'
        self.is_police = False
        self.go()

    def go(self):
        print(self.name, 'go')

    def stop(self):
        print(self.name, 'stop')

    def turn(self, direction):
        print(self.name, 'turn', direction)


class WorkCar:
    def __init__(self):
        self.speed = 30
        self.color = 'yellow'
        self.name = 'WorkCar'
        self.is_police = False
        self.go()

    def go(self):
        print(self.name, 'go')

    def stop(self):
        print(self.name, 'stop')

    def turn(self, direction):
        print(self.name, 'turn', direction)


class PoliceCar:
    def __init__(self):
        self.speed = 100
        self.color = 'black'
        self.name = 'PoliceCar'
        self.is_police = True
        self.go()

    def go(self):
        print(self.name, 'go')

    def stop(self):
        print(self.name, 'stop')

    def turn(self, direction):
        print(self.name, 'turn', direction)


town_car = TownCar()
sport_car = SportCar()
work_car = WorkCar()
work_car.stop()
police_car = PoliceCar()

town_car.turn('left')


# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.

class Car:
    def __init__(self, name, speed, color):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False
        self.go()

    def go(self):
        print(self.name, 'go')

    def stop(self):
        print(self.name, 'stop')

    def turn(self, direction):
        print(self.name, 'turn', direction)


class TownCar(Car):
    def __init__(self, color):
        self.speed = 60
        self.color = color
        self.name = 'TownCar'
        super().__init__(self.name, self.speed, self.color)


class SportCar(Car):
    def __init__(self, color):
        self.speed = 200
        self.color = color
        self.name = 'SportCar'
        super().__init__(self.name, self.speed, self.color)

class WorkCar(Car):
    def __init__(self, color):
        self.speed = 30
        self.color = color
        self.name = 'WorkCar'
        super().__init__(self.name, self.speed, self.color)

class PoliceCar(Car):
    def __init__(self, color):
        self.speed = 150
        self.color = color
        self.name = 'PoliceCar'
        super().__init__(self.name, self.speed, self.color)
        self.is_police = True

town_car = TownCar('white')
sport_car = SportCar('red')
work_car = WorkCar('yellow')
police_car = PoliceCar('black')

print(town_car.name, town_car.color, town_car.speed, town_car.is_police)
print(sport_car.name, sport_car.color, sport_car.speed, sport_car.is_police)
print(work_car.name, work_car.color, work_car.speed, work_car.is_police)
print(police_car.name, police_car.color, police_car.speed, police_car.is_police)


