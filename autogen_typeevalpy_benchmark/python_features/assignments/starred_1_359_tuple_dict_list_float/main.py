# Functions are assigned to variables via starred assignment
def func1():
    return (84, 35, 80)


def func2():
    return {'tufzp': 9, 'zslud': 25, 'nyjko': 78}


def func3():
    return [96, 16, 14]


def func4():
    return 67.19

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
