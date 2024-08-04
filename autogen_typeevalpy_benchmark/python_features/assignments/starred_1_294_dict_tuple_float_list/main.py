# Functions are assigned to variables via starred assignment
def func1():
    return {'ssfpl': 82, 'xlbck': 37, 'znyjp': 52}


def func2():
    return (83, 59, 30)


def func3():
    return 53.24


def func4():
    return [44, 49, 78]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
