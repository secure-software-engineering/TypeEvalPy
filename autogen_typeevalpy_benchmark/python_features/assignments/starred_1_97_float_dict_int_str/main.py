# Functions are assigned to variables via starred assignment
def func1():
    return 92.5


def func2():
    return {'uplqo': 35, 'wzyto': 42, 'jjggj': 85}


def func3():
    return 67


def func4():
    return 'bafkj'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
