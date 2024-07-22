# Functions are assigned to variables via starred assignment
def func1():
    return {'suaan': 69, 'gklld': 71, 'oszst': 40}


def func2():
    return 81


def func3():
    return (27, 23, 45)


def func4():
    return 62.24

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
