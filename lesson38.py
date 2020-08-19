from classes1 import Person

person1 = Person('John')
person1.print_info()

person2 = Person('Katy')
# person2.age = 30
# print(person2.get_age())
# person2.set_age(0)
print(person2.age)  # <bound method Person.age of <classes1.Person object at 0x012FD028>>
person2.age = 35
person2.print_info()