# Functions are assigned to variables via starred assignment
def func1():
    return (82, 14, 48)


def func2():
    return 16.69


def func3():
    return 'vpwwl'


def func4():
    return {'blvox': 17, 'legeh': 52, 'dytca': 59}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
