# Functions are assigned to variables via starred assignment
def func1():
    return {'rnnuc': 63, 'tkxoa': 26, 'cefhy': 71}


def func2():
    return 90.93


def func3():
    return (41, 23, 10)


def func4():
    return 'vzqit'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
