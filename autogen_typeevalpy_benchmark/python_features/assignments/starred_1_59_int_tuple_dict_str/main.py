# Functions are assigned to variables via starred assignment
def func1():
    return 42


def func2():
    return (39, 50, 99)


def func3():
    return {'rpftd': 4, 'xnelw': 56, 'enhfg': 11}


def func4():
    return 'ishtz'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
