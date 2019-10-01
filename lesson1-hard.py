print('Введите данные:')

name = input('\tИмя: ')
surname = input('\tФамилия: ')
age = int(input('\tВозраст: '))
weight = int(input('\tВес: '))

if age < 30 and weight >= 50 and weight <= 120:
    print('Хорошее состояние!')
elif age >= 40 and (weight < 50 or weight > 120):
    print('Требуется врачебный осмотр!')
elif age >= 30 and (weight < 50 or weight > 120):
    print('Нужно подумать о правильном образе жизни!')
elif weight > 120:
    print('Хватит жрать!')
elif age > 100:
    print('Столько не живут!')
else: print('Даже не знаю что и сказать')
