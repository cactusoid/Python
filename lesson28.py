# a = 5
# def f():
#     global a
#     a += 1
#     print(a)
#
# print(a)
# f()
# print(a)

l = [1, "2", 3]

def f(l):
    return [i * 2 for i in l]

print(f(l))

def f2(l):
    def get_mult(x):
        return x * 2
    return [get_mult(i) for i in l]

print(f2(l))

def f3(l):
    def get_mult(x):
        if isinstance(x, int):
            return x * 2
    return [get_mult(i) for i in l]

print(f3(l))