# Functions are assigned to variables via starred assignment
def func1():
    return (60, 94, 97)


def func2():
    return [94, 67, 61]


def func3():
    return {'nbqpw': 84, 'dhlrf': 77, 'lfpxy': 26}


def func4():
    return 21

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
