# Functions are assigned to variables via starred assignment
def func1():
    return {'yaenv': 84, 'gqvtz': 17, 'qjgxe': 58}


def func2():
    return (64, 83, 92)


def func3():
    return 76.94


def func4():
    return 8

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
