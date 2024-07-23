# Functions are assigned to variables via starred assignment
def func1():
    return 71


def func2():
    return (29, 73, 90)


def func3():
    return [53, 68, 63]


def func4():
    return {'skyji': 67, 'cqqco': 76, 'gfvma': 93}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
