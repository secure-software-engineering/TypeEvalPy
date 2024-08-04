# Functions are assigned to variables via starred assignment
def func1():
    return {'csajc': 2, 'nqrts': 58, 'dwfbf': 18}


def func2():
    return 17


def func3():
    return [31, 42, 5]


def func4():
    return (20, 96, 84)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
