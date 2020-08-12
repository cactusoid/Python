# x = 0
# if x:
#     print('Переменная х вернула ИСТИНУ')
# else:
#     print('Переменная х вернула ЛОЖЬ')
#
#
# if 1:
#     print('Выражение истинно')
# else:
#     print('Выражение ложно')
#
# light = 'red'
# if light == 'red':
#     print('Stop')
# elif light == 'yellow':
#     print('Wait')
# elif light == 'green':
#     print('Go')
# else:
#     print('What?')

# age = int(input('Сколько вам лет? '))
# if age >= 18:
#     print('Добро пожаловать')
# else:
#     print(f'Вам {age} лет, не хватает {18 - age}')

time = 11
if time < 12 or time > 13:
    print('Open')
else:
    print('Close')

x = 1
res = 'OK' if x else 'NO'
print(res)