# Functions are assigned to variables via starred assignment
def func1():
    return {'vvcpr': 80, 'ipeqj': 94, 'jzdji': 62}


def func2():
    return 72


def func3():
    return [98, 81, 70]


def func4():
    return (95, 48, 9)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
