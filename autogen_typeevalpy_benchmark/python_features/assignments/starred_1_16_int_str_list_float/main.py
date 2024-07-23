# Functions are assigned to variables via starred assignment
def func1():
    return 88


def func2():
    return 'zmabx'


def func3():
    return [6, 10, 92]


def func4():
    return 26.67

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
