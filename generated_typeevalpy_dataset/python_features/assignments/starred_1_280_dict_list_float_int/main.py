# Functions are assigned to variables via starred assignment
def func1():
    return {'gielw': 17, 'hvddn': 39, 'hdxpj': 80}


def func2():
    return [7, 29, 61]


def func3():
    return 46.41


def func4():
    return 20

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
