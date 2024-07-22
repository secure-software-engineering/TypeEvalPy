# Functions are assigned to variables via starred assignment
def func1():
    return [71, 78, 39]


def func2():
    return 53


def func3():
    return {'zejmf': 88, 'zmkmv': 74, 'exhdr': 48}


def func4():
    return (22, 29, 39)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
