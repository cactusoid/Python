"""
1. Дан массив, в котором среди прочих элементов есть слово "odd" (нечётный). Определите, есть
ли в списке число, которое является индексом элемента "odd". Напишите функцию, которая будет возвращать
True или False, соответственно.
"""

def odd_ball(arr):
    for i in list(arr):
        k = arr.index('odd')
        if i == k:
            return True
    return False


print(odd_ball(['even', 4, 'even', 7, 'even', 55, 'even', 6, 'even', 10, 'odd', 3, 'even']))  # True
print(odd_ball(['even', 4, 'even', 7, 'even', 55, 'even', 6, 'even', 9, 'odd', 3, 'even']))  # False
print(odd_ball(['even', 10, 'odd', 2, 'even']))  # True


'''
2. Напишите функцию find_sum(n), где аргумент функции - это конечный элемент последовательности включительно.
Функция должна вернуть сумму всех чисел последовательности, кратных 3 или 5. Попробуйте решить задачу двумя
способами (один из способов в одну строчку кода). 
'''

def find_sum(n):
    print(sum([i for i in range(n + 1) if i % 3 == 0 or i % 5 == 0]))


find_sum(5)
find_sum(10)



'''
3. Дан список имён. Выберите в новый список только те имена, которые состоят из четырёх букв.
names = ['Ryan', 'Kieran', 'Mark', 'John', 'David', 'Paul']
'''

def get_names(names):
    for i in range(len(names)):
        if len(names[i]) == 4:
            names1.append(names[i])
    print(names1)
names1 =[]
get_names(['Ryan', 'Kieran', 'Mark', 'John', 'David', 'Paul'])
