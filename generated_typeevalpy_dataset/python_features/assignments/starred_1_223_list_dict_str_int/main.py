# Functions are assigned to variables via starred assignment
def func1():
    return [20, 99, 5]


def func2():
    return {'vrfmx': 7, 'sdprv': 21, 'tksbs': 47}


def func3():
    return 'xccex'


def func4():
    return 71

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
