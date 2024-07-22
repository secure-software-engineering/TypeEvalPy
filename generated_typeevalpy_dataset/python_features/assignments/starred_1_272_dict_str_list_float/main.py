# Functions are assigned to variables via starred assignment
def func1():
    return {'ezpgi': 91, 'pdvtu': 47, 'jvpzb': 61}


def func2():
    return 'zvuxi'


def func3():
    return [58, 19, 46]


def func4():
    return 55.16

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
