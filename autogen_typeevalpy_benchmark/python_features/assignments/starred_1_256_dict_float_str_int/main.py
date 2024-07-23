# Functions are assigned to variables via starred assignment
def func1():
    return {'qodkk': 41, 'uirbt': 93, 'atwxk': 46}


def func2():
    return 82.75


def func3():
    return 'tbwtp'


def func4():
    return 58

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
