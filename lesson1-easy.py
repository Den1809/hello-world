# Task 1
str='Привет'
name = input('Введите имя: ')
print(str,name)

# Task 2
number = int(input('Введите число: '))
print(number+2)

#Task 3
age = int(input('Введите ваш возраст: '))

if age >= 18:
    print('Доступ разрешен')
elif age < 0:
    print('Так не бывает')
else:
    print('Извините, пользование данным ресурсом только с 18 лет')