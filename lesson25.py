'''
Создайте игру "Угадай число". В коде программы в переменную запишите любое число от 1 до 100
(в следующих уроках мы узнаем, как генерировать случайное число), которое и должен угадать игрок. Далее программа
должна спросить у игрока угадать число. Если пользователь не угадал число - программа сообщает, что загаданное
число больше/меньше и предлагает ещё раз, при этом программа ведёт счёт количества попыток игрока.
Если игрок угадал число, тогда программа благодарит за игру и сообщает количество попыток, за которое было угадано
число.
'''


nums = 75
i = 1
nums1 = int(input('Угадайте число: '))
while nums != nums1:
    i += 1
    if nums1 < nums:
        print('Загаданное число больше')
        nums1 = int(input('Угадайте число: '))
    elif nums1 > nums:
        print('Загаданное число меньше')
        nums1 = int(input('Угадайте число: '))
print('Вы угадали, благодарим за игру')
print('Количество попыток: ', i)


x = 75
user_num = 0
cnt = 0
while True:
    user_num = int(input('Угадай число от 1 до 100: '))
    cnt += 1
    if user_num == x:
        print(f'Вы угадали число за {cnt} попыток')
        print('Благодарим за игру')
        break
    elif user_num > x:
        print('Загаданное число меньше')
    else:
        print('Загаданное число больше')