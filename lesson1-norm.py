min_number, max_number = 0, 10
number = int(input('Введите число от ' + str(min_number) + ' до ' + str(max_number) + ': '))

while not (number > min_number and number < max_number):
    print('Некорректное значение')
    number = int(input('Введите число от ' + str(min_number) + ' до ' + str(max_number) + ': '))

print('Результат: ', str(number ** 2))
