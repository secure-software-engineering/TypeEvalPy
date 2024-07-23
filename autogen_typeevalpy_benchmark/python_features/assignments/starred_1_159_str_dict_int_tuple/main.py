# Functions are assigned to variables via starred assignment
def func1():
    return 'rmbtv'


def func2():
    return {'njufy': 90, 'okdwq': 22, 'jxvou': 37}


def func3():
    return 5


def func4():
    return (45, 23, 24)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
