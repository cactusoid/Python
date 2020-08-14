# https://docs.python.org/3/library/

# import os
# import random можно написать так:
# import random as r
# from random import randint, shuffle

# print(os.getcwd())

# print(random.randint(1, 100)) тогда можно будет сокращённо писать:
# print(r.randint(1, 100))
# shuffle - это перемешивание
# print(randint(1, 100))
# l = [1, 2, 3, 4, 5]
# shuffle(l)
# print(l)

import libs

print(libs.get_count('hello', 'l'))  # 2
print(libs.get_len('hello'))  # 5

# можно написать так:
f = libs.get_count
print(f('hello', 'l'))  # 2

def get_sum(a, b):
    return a + b

func = get_sum
print(func(1, 2))