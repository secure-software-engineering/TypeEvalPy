# Functions are assigned to variables via starred assignment
def func1():
    return [77, 61, 38]


def func2():
    return {'rnxer': 16, 'nasnx': 61, 'upwnw': 54}


def func3():
    return (40, 22, 17)


def func4():
    return 'cjjxz'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
