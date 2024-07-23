# Functions are assigned to variables via starred assignment
def func1():
    return (85, 26, 98)


def func2():
    return {'qisty': 21, 'xdqry': 90, 'zinzv': 13}


def func3():
    return [35, 59, 4]


def func4():
    return 'qdcjs'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
