import re

# s = 'Это просто строка текста. А это ещё одна строка текста.'
# pattern = 'строка'

# if re.search(pattern, s):
#     print('Matched')
# else:
#     print('No match')
#
# match = re.search(pattern, s)
# print(match)  # <re.Match object; span=(11, 17), match='строка'>
# print(match.span())  # (11, 17)
# print(match.start())  # 11
# print(match.end())  # 17

# print(re.findall(pattern, s))  # ['строка', 'строка']

# print(re.split(r'\.', s))  # ['Это просто строка текста', ' А это ещё одна строка текста', '']
# print(re.split(r'\.', s, 1))  # ['Это просто строка текста', ' А это ещё одна строка текста.']

s = '''Это просто строка текста.
А это ещё одна строка текста.
А это строка с цифрами: 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 10
А это строка с разными символами: "!", "@", "-", "&", "?", "_"
a\\b\tc
test string'''

# pattern = r'\w+'
# pattern = r'[эт]'
# pattern = r'[а-я]+'
# pattern = r'[а-я0-9]+'
# pattern = r'[а-яА-Яё]+'
# pattern = r'[а-яё]+'
# pattern = r'[0-9]+'
# pattern = r'\d+'
# pattern = r'[\d-]+'
# pattern = r'\w+$'

# print(re.findall(pattern, s, flags=re.IGNORECASE))

def validate_email(email):
    # return re.match(r'^.+@(\w+\.){0,2}[a-z]{2,6}$', email, re.IGNORECASE)
    return bool(re.match(r'^.+@(\w+\.){0,2}[a-z]{2,6}$', email, re.IGNORECASE))


print(validate_email('mail@mail.com'))
print(validate_email('ivanov@gmail.com.ua'))
print(validate_email('kuda@bank'))

'''
<re.Match object; span=(0, 13), match='mail@mail.com'>
<re.Match object; span=(0, 19), match='ivanov@gmail.com.ua'>
<re.Match object; span=(0, 9), match='kuda@bank'>
'''