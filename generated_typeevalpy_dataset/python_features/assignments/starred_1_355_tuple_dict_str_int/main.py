# Functions are assigned to variables via starred assignment
def func1():
    return (33, 56, 7)


def func2():
    return {'qjndu': 39, 'xaftz': 53, 'bgjpv': 69}


def func3():
    return 'sygpa'


def func4():
    return 26

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
