# Functions are assigned to variables via starred assignment
def func1():
    return 33


def func2():
    return 'negcr'


def func3():
    return {'qtdqf': 65, 'carbs': 13, 'fyasb': 26}


def func4():
    return 43.38

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
