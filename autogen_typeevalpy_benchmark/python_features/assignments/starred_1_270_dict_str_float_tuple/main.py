# Functions are assigned to variables via starred assignment
def func1():
    return {'qvtex': 72, 'upcwf': 17, 'mexbb': 19}


def func2():
    return 'nqlhl'


def func3():
    return 6.36


def func4():
    return (37, 80, 72)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
