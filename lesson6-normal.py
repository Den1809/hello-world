# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.

class Player:
    def __init__(self, name, health, damage, armor):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor

    def _defense(self, victim, damage):
        return(damage/victim.armor)

    def attack(self, attacker, victim):
        victim.health -= int(self._defense(victim,attacker.damage))
        if int(victim.health) < 0: victim.health = 0

class Player1(Player):
    def __init__(self, name):
        self.health = 100
        self.damage = 30
        self.armor = 1.2
        self.name = name
        super().__init__(name, self.health, self.damage, self.armor)

class Player2(Player):
    def __init__(self, name):
        self.health = 100
        self.damage = 20
        self.armor = 1.5
        self.name = name
        super().__init__(name, self.health, self.damage, self.armor)

player1 = Player1('Вася')
player2 = Player2('Петя')

i = 0
while True:
    i +=1
    if i % 2 != 0:
        player1.attack(player1, player2)
        print(f'Атака {i} (атакует',player1.name,'): \n\tИгрок', player1.name, ': ', player1.health, '\n\tИгрок', player2.name, ': ', player2.health)
    else:
        player2.attack(player2, player1)
        print(f'Атака {i} (атакует',player2.name,'): \n\tИгрок', player1.name, ': ', player1.health, '\n\tИгрок', player2.name, ': ', player2.health)

    if player1.health <= 0:
        print('Победил игрок',player2.name,'\nСчет:',player2.health,':',player1.health)
        break
    if player2.health <= 0:
        print('Победил игрок',player1.name,'\nСчет:',player1.health,':',player2.health)
        break