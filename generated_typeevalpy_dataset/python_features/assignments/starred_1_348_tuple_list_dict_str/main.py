# Functions are assigned to variables via starred assignment
def func1():
    return (13, 74, 92)


def func2():
    return [61, 42, 80]


def func3():
    return {'pdpkc': 63, 'weqmo': 59, 'xiilj': 84}


def func4():
    return 'lafrs'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
