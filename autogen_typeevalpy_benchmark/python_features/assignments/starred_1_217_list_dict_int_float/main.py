# Functions are assigned to variables via starred assignment
def func1():
    return [64, 52, 81]


def func2():
    return {'lnmic': 21, 'ffuhn': 79, 'ubacf': 40}


def func3():
    return 80


def func4():
    return 93.75

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
