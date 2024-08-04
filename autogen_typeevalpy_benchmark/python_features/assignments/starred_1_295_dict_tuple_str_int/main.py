# Functions are assigned to variables via starred assignment
def func1():
    return {'azhrx': 46, 'tltfs': 69, 'qbrhp': 60}


def func2():
    return (89, 57, 4)


def func3():
    return 'awxgp'


def func4():
    return 41

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
