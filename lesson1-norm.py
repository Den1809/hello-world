#Task 1

min_number, max_number = 0, 10
number = int(input('Введите число от ' + str(min_number) + ' до ' + str(max_number) + ': '))

while not (number > min_number and number < max_number):
    print('Некорректное значение')
    number = int(input('Введите число от ' + str(min_number) + ' до ' + str(max_number) + ': '))

print('Результат: ', str(number ** 2))

#Task2

a = int(input('Ввод 1: '))
b = int(input('Ввод 2: '))

print(a, b)

a, b = b, a
print(a, b)

a = a + b
b = a - b
a = a - b
print(a, b)
