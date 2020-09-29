class SchoolMembers:
    """Участник школы"""

    def __init__(self, firstname, lastname, age):
        """Определяет имя и фамилию участника школы"""
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def tell(self):
        print("Имя: %s; Фамилия: %s; Возраст: %d;"%(self.firstname, self.lastname, self.age))

class Student(SchoolMembers):
    def __init__(self, firstname, lastname, age, graduate):
        SchoolMembers.__init__(self, firstname, lastname, age)
        self.graduate = graduate

    def tell(self):
        SchoolMembers.tell(self)
        print("Учится в %d классе"%self.graduate)

class Teacher(SchoolMembers):

    def __init__(self, firstname, lastname, age, salary):
        super().__init__(firstname, lastname, age)
        self.salary = salary

    def tell(self):
        super().tell()
        print("Зарплата: %d  рублей в месяц"%self.salary)


while True:
    print(" 1 - Добавить ученика, 2 - Добавить учителя, 3 - выход")
    choice = int(input("Что выберите вы: "))
    if choice == 1:
        name = input("Введите имя ученика: ")
        lastname = input("Введите фамилию ученика: ")
        age = int(input("Введите его возраст: "))
        graduate = int(input("В каком он классе: "))
        newstudent = Student(name, lastname, age, graduate)
        newstudent.tell()

    elif choice == 2:
        name = input("Введите имя учителя: ")
        lastname = input("Введите фамилию учителя: ")
        age = int(input("Введите его возраст: "))
        salary = int(input("Какая у него зарплата в месяц: "))
        newteacher = Teacher(name, lastname, age, salary)
        newteacher.tell()

    elif choice == 3:
        print("Всего вам доброго!")
        break

    else:
        continue