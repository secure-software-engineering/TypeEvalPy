# Functions are assigned to variables via starred assignment
def func1():
    return (87, 67, 28)


def func2():
    return {'rcjgc': 51, 'ntvki': 56, 'jcrai': 56}


def func3():
    return 95


def func4():
    return 65.29

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
