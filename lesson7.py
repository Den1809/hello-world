#!/usr/bin/python3

"""
== Лото ==
Правила игры в лото.
Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------
В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.
Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.
Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.
Пример одного хода:
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87
      16 49    55 77    88
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)
Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.
Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html
"""
import random


class Card():
    def __init__(self):
        self.CARD_ROWS = 3
        self.CARD_COLUMNS = 9
        self.CARD_SIZE = self.CARD_ROWS * self.CARD_COLUMNS
        self.MAX_FILLED_COLUMNS = 5
        self.NUM_COUNT = 90

        self.card_values = []
        self.init_card()

    def value_in_card(self, value):
        is_value_in_card = False
        for row in self.card_values:
            if (value in row) or is_value_in_card:
                is_value_in_card = True
        return is_value_in_card

    def init_card(self):
        self.card_values = []
        self.filled_nums = 0
        while len(self.card_values) <= self.CARD_ROWS - 1:
            card_row = []
            while len(card_row) <= self.CARD_COLUMNS - 1:
                pool_value = str(random.randint(1, self.NUM_COUNT))
                if (not self.value_in_card(pool_value)) and (pool_value not in card_row):
                    card_row.append(pool_value)
                    self.filled_nums += 1
            card_row.sort(key=int)
            self.card_values.append(card_row)
        print(self.filled_nums)

        # вариант с прямой адресацией списка
        #     i = 0
        #     while i <= self.CARD_ROWS-1:
        #         self.card_values.append([])
        #         j = 0
        #         while j <= self.CARD_COLUMNS-1:
        #             pool_value = str(random.randint(1, self.NUM_COUNT))
        #             if (not self.value_in_card(pool_value)):
        #                 self.card_values[i].append(pool_value)
        #                 j += 1
        #         self.card_values[i].sort(key=int)
        #         i += 1

        i = 0
        while i <= len(self.card_values) - 1:
            while self.card_values[i].count(' ') < self.CARD_COLUMNS - self.MAX_FILLED_COLUMNS:
                empty_pos = random.randint(0, self.CARD_COLUMNS - 1)
                if self.card_values[i][empty_pos] != ' ':
                    self.card_values[i][empty_pos] = ' '
                    self.filled_nums -=1
            i += 1
        print(self.filled_nums)

    def show_card(self):
        # print(self.card_values)
        print(str.rjust('', self.CARD_COLUMNS * (len(str(self.NUM_COUNT)) + 1) + 1, '-'))
        for row in self.card_values:
            row_str = ''
            for value in row:
                row_str += str(value).rjust(len(str(self.NUM_COUNT)) + 1, ' ')
            print(row_str)
        print(str.rjust('', self.CARD_COLUMNS * (len(str(self.NUM_COUNT)) + 1) + 1, '-'))

    def mark_value(self, value):
        i = 0
        for row in self.card_values:
            if value in row:
                try:
                    self.card_values[i][list(row).index(value)] = '-'
                    self.filled_nums -= 1
                except:
                    pass
            i += 1

class Barrels():
    def __init__(self):
        self.MAX_BARREL_COUNT = 90
        self.init_barrels()

    def init_barrels(self):
        self._barrel_pool = [str(i) for i in range(1, self.MAX_BARREL_COUNT+1)]
        random.shuffle(self._barrel_pool)

    def get_barrel(self):
        random.shuffle(self._barrel_pool)
        return self._barrel_pool.pop()

    def get_barrel_count(self):
        return len(self._barrel_pool)

    def _show_barrels(self):
        print(self._barrel_pool)

class Player(Card):
    def __init__(self, name):
        if name == 'Компьютер':
            self.is_comp = True
        else:
            self.is_comp = False
        self.name = name
        super().__init__()

    def show_card(self):
        if not self.is_comp:
            print('Игрок', self.name)
        else:
            print('Компьютер')
        super().show_card()


class Game:
    def __init__(self, player, comp):
        self.player = player
        self.comp = comp

    def start(self):
        self.barrels = Barrels()

        i = 0
        while True:#(self.barrels.get_barrel_count() > 0) and (self.player.filled_nums > 0 and self.comp.filled_nums > 0):
            i += 1
            barrel = self.barrels.get_barrel()
            print('Ход № {}. Счет {}:{}'.format(i, self.player.MAX_FILLED_COLUMNS*self.player.CARD_ROWS-self.player.filled_nums,
                                                self.comp.MAX_FILLED_COLUMNS*self.comp.CARD_ROWS-self.comp.filled_nums))
            print('Новый бочонок: {} (осталось {})'.format(barrel, self.barrels.get_barrel_count()))

            self.player.show_card()
            self.comp.show_card()

            if self.comp.value_in_card(barrel):
                self.comp.mark_value(barrel)

            self.player.mark_value(barrel)
            choice = input('Зачеркнуть цифру? y/n')
            if choice.upper() == 'Y':
                if self.player.value_in_card(barrel):
                    self.player.mark_value(barrel)
                else:
                    print('Выиграл',self.comp.name)
                    break
            else:
                if not self.player.value_in_card(barrel):
                    pass
                else:
                    print('Выиграл',self.comp.name)
                    break

            if self.player.filled_nums == 0 and self.comp.filled_nums > 0:
                print('Выиграл игрок',self.player.name)
                break
            if self.comp.filled_nums == 0 and self.player.filled_nums > 0:
                print('Выиграл', self.comp.name)
                break
            if (self.comp.filled_nums == 0 and self.player.filled_nums == 0) or self.barrels.get_barrel_count() == 0:
                print('Ничья!')
                break
        print('Счет {}:{}'.format(self.player.MAX_FILLED_COLUMNS * self.player.CARD_ROWS - self.player.filled_nums,
                                  self.comp.MAX_FILLED_COLUMNS * self.comp.CARD_ROWS - self.comp.filled_nums))


player_name = ('Введите имя игрока:')
human = Player(player_name)
comp = Player('Компьютер')
game = Game(human, comp)

game.start()
