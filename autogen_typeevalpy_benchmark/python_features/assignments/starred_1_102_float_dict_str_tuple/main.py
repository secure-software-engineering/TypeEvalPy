# Functions are assigned to variables via starred assignment
def func1():
    return 20.33


def func2():
    return {'kmdwp': 97, 'bclqd': 76, 'kzfeq': 47}


def func3():
    return 'pcrrs'


def func4():
    return (91, 62, 3)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
