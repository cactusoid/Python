from classes1 import Person, Employee

person = Person('Katy', 30)
person.age = 35
person.print_info()
print(Person)

employee = Employee('Nick', 30, 'Google')
employee.print_info()
employee.more_info()
print(employee)  # <classes1.Employee object at 0x0149D028>