# Functions are assigned to variables via starred assignment
def func1():
    return {'zaoxj': 49, 'nmyuc': 91, 'jyedf': 67}


def func2():
    return 59.92


def func3():
    return 'janhl'


def func4():
    return [96, 10, 17]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
