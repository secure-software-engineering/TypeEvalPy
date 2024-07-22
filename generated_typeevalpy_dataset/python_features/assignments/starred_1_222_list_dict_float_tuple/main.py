# Functions are assigned to variables via starred assignment
def func1():
    return [26, 55, 5]


def func2():
    return {'amwzi': 93, 'vuntw': 70, 'oyfnh': 11}


def func3():
    return 53.18


def func4():
    return (70, 73, 100)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
