# Functions are assigned to variables via starred assignment
def func1():
    return (79, 99, 72)


def func2():
    return 'kqyoi'


def func3():
    return [56, 35, 46]


def func4():
    return {'ufotp': 30, 'kjydb': 24, 'oecyx': 7}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
