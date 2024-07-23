# Functions are assigned to variables via starred assignment
def func1():
    return 83


def func2():
    return [12, 9, 16]


def func3():
    return {'pidza': 82, 'fdwyu': 70, 'yxinp': 85}


def func4():
    return (53, 30, 28)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
