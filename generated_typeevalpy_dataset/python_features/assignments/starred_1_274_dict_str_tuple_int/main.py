# Functions are assigned to variables via starred assignment
def func1():
    return {'uerct': 64, 'ojyxs': 80, 'yaqtn': 66}


def func2():
    return 'irjdi'


def func3():
    return (5, 64, 91)


def func4():
    return 85

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
