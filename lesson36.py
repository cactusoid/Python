class A:
    property1 = 'Property 1'
    property2 = 'Property 2'
    name = 'Anonymous'

    def say_hi(self, name=''):
        if name:
            return 'Hi, ' + name
        else:
            return 'Hello, ' + self.name


a = A()
b = A()
# a.property1 = 'Property 1'
# a.property2 = 'Property 2'
# print(a)  # <__main__.A object at 0x01CFD028>
print(a.property2)  # Property 2
print(a.say_hi())  # Hello, Anonymous
print(a.say_hi('John'))  # Hi, John
print(a.say_hi('Katy'))  # Hi, Katy