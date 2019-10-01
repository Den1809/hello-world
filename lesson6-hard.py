# Задача - 1
# Вам необходимо создать завод по производству мягких игрушек для детей.
# Вам надо продумать структуру классов,
# чтобы у вас был класс, который создает игрушки на основании:
#  Названия, Цвета, Типа (животное, персонаж мультфильма)
# Опишите процедуры создания игрушки в трех методах:
# -- Закупка сырья, пошив, окраска
# Не усложняйте пусть методы просто выводят текст о том, что делают.
# В итоге ваш класс по производству игрушек должен вернуть объект нового класса Игрушка.

# class Toy:
#     def __init__(self, name, color, type):
#         self.name = name
#         self.color = color
#         self.type = type
#
# class Factory(Toy):
#
#     def prepare(self):
#         print(self.type, self.name, 'Закупка сырья')
#
#     def work(self):
#         print(self.type, self.name, 'Пошив')
#
#     def paint(self):
#         print(self.type,self.name, self.color,'Покраска')
#
# toy1 = Factory('Тигр', 'Желто-полосатый', 'Животное')
# print(toy1.name, toy1.color, toy1.type)
# toy1.prepare()
# toy1.work()
# toy1.paint()
# toy2 = Factory('Буратино', 'Древесно-струженный', 'Персонаж')
# print(toy2.name, toy2.color, toy2.type)
# toy2.prepare()
# toy2.work()
# toy2.paint()

# Задача - 2
# Доработайте нашу фабрику, создайте по одному классу на каждый тип, теперь надо в классе фабрика
# исходя из типа игрушки отдавать конкретный объект класса, который наследуется от базового - Игрушка

class Toy:
    def __init__(self, name, color, type):
        self.name = name
        self.color = color
        self.type = type

class AnimalToy(Toy):
    def __init__(self, name, color):
        self.type = 'Животное'
        self.name = name
        self.color = color
        print(__class__,'создан')

class PersonToy(Toy):
    def __init__(self, name, color):
        self.type = 'Персонаж'
        self.name = name
        self.color = color
        print(__class__,'создан')

class Factory(Toy):
    def __init__(self, name, color, type):
        if type == 'Животное':
            AnimalToy.__init__(self, name, color)
        else:
            PersonToy.__init__(self, name, color)

    def prepare(self):
        print(self.name,'Закупка сырья')

    def work(self):
        print(self.name,'Пошив')

    def paint(self):
        print(self.name,'Покраска')

animal = Factory('Тигр', 'Желто-полосатый','Животное')
person = Factory('Буратино', 'Древесно-струженный','Персонаж')

print(animal.name, animal.color, animal.type)
print(person.name, person.color, person.type)

animal.prepare()
person.prepare()