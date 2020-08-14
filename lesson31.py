'''
Создайте игру "Угадай число". В коде программы в переменную запишите любое число от 1 до 100
(в следующих уроках мы узнаем, как генерировать случайное число), которое и должен угадать игрок. Далее программа
должна спросить у игрока угадать число. Если пользователь не угадал число - программа сообщает, что загаданное
число больше/меньше и предлагает ещё раз, при этом программа ведёт счёт количества попыток игрока.
Если игрок угадал число, тогда программа благодарит за игру и сообщает количество попыток, за которое было угадано
число.
'''
import random

# nums = random.randint(1, 100)
# i = 1
# nums1 = int(input('Угадайте число: '))
# while nums != nums1:
#     i += 1
#     if nums1 < nums:
#         print('Загаданное число больше')
#         nums1 = int(input('Угадайте число: '))
#     elif nums1 > nums:
#         print('Загаданное число меньше')
#         nums1 = int(input('Угадайте число: '))
# print('Вы угадали, благодарим за игру')
# print('Количество попыток: ', i)


# x = random.randint(1, 100)
# user_num = 0
# cnt = 0
# while True:
#     user_num = int(input('Угадай число от 1 до 100: '))
#     cnt += 1
#     if user_num == x:
#         print(f'Вы угадали число за {cnt} попыток')
#         if input('Сырграем ещё? "y | n": ') == 'y':
#             x = random.randint(1, 100)
#             cnt = 0
#         else:
#             print('Благодарим за игру')
#             break
#     elif user_num > x:
#         print('Загаданное число меньше')
#     else:
#         print('Загаданное число больше')


from datetime import date, datetime, timedelta

import locale

# date
# today = date.today()
# print(today)  # 2020-08-14
# print(today.day)  # 14
# print(today.month)  # 8
# print(today.year)  # 2020
# print(today.weekday())  # 4, пятница 4 день, так как понедельник нулевой день.

# datetime
# now = datetime.now()
# now2 = datetime.today()

# print(now, now2, sep='\n')
# print(now)  # 2020-08-14 14:49:58.186195
# print(now.day)  # 14
# print(now.month)  # 8
# print(now.year)  # 2020
# print(now.weekday())  # 4
# print(now.hour)  # 14
# print(now.minute)  # 56
# print(now.second)  # 3
#
# days = ['пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс']
# print(days[now.weekday()])  # пт

# locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
# locale.setlocale(locale.LC_ALL, 'ru_RU')
# now = datetime.now()
# print(now)
#
# print(now.strftime('%a'))
# print(now.strftime('%A'))
#
# print(f'Дата: {now.strftime("%A, %d %b %Y")}')
# print(f'Время: {now.strftime("%H:%M:%S")}')
#
# print(now.strftime('%c'))
# print(now.strftime('%x'))
# print(now.strftime('%X'))

now = datetime.today()
print(now.strftime('%c'))
d1 = now + timedelta(days=1, hours=2, minutes=10)
print(d1.strftime('%c'))