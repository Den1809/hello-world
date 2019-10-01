# Задание - 1
# Давайте опишем пару сущностей player и enemy через словарь,
# который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health - 100,
# damage - 50.
# Поэксперементируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, person2), аргументы можете указать свои,
# функция в качестве аргумента будет принимать атакующего и атакуемого,
# функция должна получить параметр damage атакующего и отнять это количество
# health от атакуемого. Функция должна сама работать с словарями и изменять их значения.

# player1 = {'name': '', 'health': 100, 'damage': 30, 'armor': 1.2}
# player2 = {'name': '', 'health': 100, 'damage': 20, 'armor': 1.5}
#
# def defense(victim, damage):
#     return(damage/victim['armor'])
#
# def attack(attacker, victim):
#     victim['health'] -= round(defense(victim,attacker['damage']),1)
#
# player1['name'] = input('Введите имя Игрока 1: ').title()
# player2['name'] = input('Введите имя Игрока 2: ').title()
#
# attack(player1, player2)
# print('Атака 1 (остаток жизни): \n\tИгрок',player1['name'],': ',player1['health'],'\n\tИгрок',player2['name'],': ',player2['health'])
# attack(player2, player1)
# print('Атака 2 (остаток жизни): \n\tИгрок',player1['name'],': ',player1['health'],'\n\tИгрок',player2['name'],': ',player2['health'])

# Задание - 2
# Давайте усложним предыдущее задание, измените сущности, добавив новый параметр - armor = 1.2
# Теперь надо добавить функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно у вас должно быть 2 функции, одна наносит урон, вторая вычисляет урон по отношению к броне.

# Сохраните эти сущности, полностью, каждую в свой файл,
# в качестве названия для файла использовать name, расширение .txt
# Напишите функцию, которая будет считывать файл игрока и его врага, получать оттуда данные, и записывать их в словари,
# после чего происходит запуск игровой сессии, где сущностям поочередно наносится урон,
# пока у одного из них health не станет меньше или равен 0.
# После чего на экран должно быть выведено имя победителя, и количество оставшихся единиц здоровья.

player1 = {}
player2 = {}

def defense(victim, damage):
    return(damage/victim['armor'])

def attack(attacker, victim):
    victim['health'] -= int(defense(victim,attacker['damage']))
    if victim['health'] < 0: victim['health'] =0

with open('player1.txt', 'r', encoding='utf-8') as file:
    for line in file:
        player1.update(dict([line.strip().split(':')]))

player1['damage']=int(player1['damage'])
player1['health']=int(player1['health'])
player1['armor']=float(player1['armor'])

with open('player2.txt', 'r', encoding='utf-8') as file:
    for line in file:
        player2.update(dict([line.strip().split(':')]))

player2['damage']=int(player2['damage'])
player2['health']=int(player2['health'])
player2['armor']=float(player2['armor'])

player1['name'] = input('Введите имя Игрока 1: ').title()
player2['name'] = input('Введите имя Игрока 2: ').title()

i = 0
while True:
    i +=1
    if i % 2 != 0:
        attack(player1, player2)
        print(f'Атака {i} (атакует',player1['name'],'): \n\tИгрок', player1['name'], ': ', player1['health'], '\n\tИгрок', player2['name'], ': ', player2['health'])
    else:
        attack(player2, player1)
        print(f'Атака {i} (атакует',player2['name'],'): \n\tИгрок', player1['name'], ': ', player1['health'], '\n\tИгрок', player2['name'], ': ', player2['health'])

    if player1['health'] <= 0:
        print('Победил игрок',player2['name'],'\nСчет:',player2['health'],':',player1['health'])
        break
    if player2['health'] <= 0:
        print('Победил игрок',player1['name'],'\nСчет:',player1['health'],':',player2['health'])
        break

