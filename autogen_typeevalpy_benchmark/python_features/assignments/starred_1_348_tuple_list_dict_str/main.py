# Functions are assigned to variables via starred assignment
def func1():
    return (70, 29, 60)


def func2():
    return [80, 86, 21]


def func3():
    return {'lafdv': 82, 'fzzln': 74, 'qgzno': 5}


def func4():
    return 'flxmx'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
