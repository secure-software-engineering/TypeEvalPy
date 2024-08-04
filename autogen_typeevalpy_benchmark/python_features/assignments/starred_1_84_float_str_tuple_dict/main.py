# Functions are assigned to variables via starred assignment
def func1():
    return 40.59


def func2():
    return 'riybp'


def func3():
    return (90, 85, 40)


def func4():
    return {'jundh': 98, 'sotpe': 12, 'cmueq': 54}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
