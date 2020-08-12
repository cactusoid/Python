a = 5
def f():
    global a
    a += 1
    print(a)

print(a)
f()
print(a)