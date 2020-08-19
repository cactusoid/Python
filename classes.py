class Person:
    name = 'John'

    def __init__(self, name):
        # print('Hi')
        self.name = name
    def print_info(self):
        print(f'Hello, my name is {self.name}')
