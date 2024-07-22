# Functions are assigned to variables via starred assignment
def func1():
    return {'yonmn': 98, 'yxmft': 95, 'skauo': 61}


def func2():
    return 39


def func3():
    return (17, 59, 4)


def func4():
    return 'ajgzr'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
