# Functions are assigned to variables via starred assignment
def func1():
    return [17, 29, 37]


def func2():
    return {'bjmwz': 65, 'cjrnt': 2, 'vcnqu': 44}


def func3():
    return 9


def func4():
    return (53, 52, 56)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
