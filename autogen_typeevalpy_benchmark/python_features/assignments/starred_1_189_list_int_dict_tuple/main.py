# Functions are assigned to variables via starred assignment
def func1():
    return [18, 59, 1]


def func2():
    return 18


def func3():
    return {'oczrs': 67, 'kdcct': 84, 'wcspk': 89}


def func4():
    return (96, 51, 81)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
