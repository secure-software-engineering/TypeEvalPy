# Functions are assigned to variables via starred assignment
def func1():
    return 'uzlgy'


def func2():
    return (22, 82, 64)


def func3():
    return {'vlioz': 72, 'ulhrp': 14, 'xwhvu': 75}


def func4():
    return 24

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
