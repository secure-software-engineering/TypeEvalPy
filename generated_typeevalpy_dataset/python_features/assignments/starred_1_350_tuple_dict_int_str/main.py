# Functions are assigned to variables via starred assignment
def func1():
    return (41, 74, 92)


def func2():
    return {'mwcfq': 95, 'tenyl': 96, 'aublf': 41}


def func3():
    return 98


def func4():
    return 'mtcwz'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
