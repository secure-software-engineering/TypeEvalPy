# Functions are assigned to variables via starred assignment
def func1():
    return 97.85


def func2():
    return (84, 29, 24)


def func3():
    return 'mmulw'


def func4():
    return [14, 26, 63]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
