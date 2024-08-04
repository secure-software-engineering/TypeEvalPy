# Functions are assigned to variables via starred assignment
def func1():
    return 87


def func2():
    return {'jercb': 78, 'jffsj': 81, 'hygtz': 11}


def func3():
    return (75, 30, 42)


def func4():
    return [13, 11, 62]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
