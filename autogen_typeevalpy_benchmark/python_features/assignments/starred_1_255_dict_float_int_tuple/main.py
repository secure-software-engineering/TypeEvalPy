# Functions are assigned to variables via starred assignment
def func1():
    return {'xsheu': 39, 'hghof': 71, 'powcl': 67}


def func2():
    return 41.61


def func3():
    return 36


def func4():
    return (15, 76, 43)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
