'''
Дан список words. Составьте из него список слов-палиндромов. Попробуйте это сделать двумя способами:
произвольное решение и решение в одну строчку кода.
Дан список my_str со строками, часть из которых являются палиндромами. Составьте новый список строк-палиндромов.
'''

words = ['мадам', 'топот', 'test', 'madam', 'word']
my_str = ['Око за око', 'А роза упала на лапу азора', 'Около Миши молоко']

# for i in range(len(words) - 1):
#     for j in range(len(words) -1):
#         print(words[i][j])

# list1 = []

# for i in range(len(words)):
#     # rev =
#     if ''.join(list(words[i][::-1])) == words[i]:
#        list1.append(words[i])


# [list1.append(words[i]) for i in range(len(words)) if ''.join(list(words[i][::-1])) == words[i]]
# print(list1)

# s = [i for i in words if i == i[::-1]]
# print(s)
#
# palindromes1 = []
# for i in my_str:
#     a = i
#     i = (i.replace(' ', '')).lower()
#     if i == i[::-1]:
#         palindromes1.append(a)
#     else:
#         continue
# print(palindromes1)


# Первая задача

# words = ['мадам', 'топот', 'test', 'madam', 'word']
# palindromes = []
#
# for word in words:
#     if word == word[::-1]:
#         palindromes.append(word)
#
# print(palindromes)

# palindromes = [word for word in words if word == word[::-1]]
# print(palindromes)


# my_str = ['Око за око', 'А роза упала на лапу азора', 'Около Миши молоко']
# palindromes = []
# for word in my_str:
#     word_r = word.replace(' ', '').lower()
#     if word_r == word_r[::-1]:
#         palindromes.append(word)
# print(palindromes)

l = list(range(1, 10))
l2 = list('hello')
print(l, l2)  # [1, 2, 3, 4, 5, 6, 7, 8, 9] ['h', 'e', 'l', 'l', 'o']
s = '-'.join(map(str, l))
s2 = ','.join(l2)
print(s)  # 1-2-3-4-5-6-7-8-9
print(s2)  # h,e,l,l,o
