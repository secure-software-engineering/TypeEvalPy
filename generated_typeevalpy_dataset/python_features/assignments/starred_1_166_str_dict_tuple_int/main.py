# Functions are assigned to variables via starred assignment
def func1():
    return 'znafl'


def func2():
    return {'twspo': 13, 'spzml': 67, 'mtajc': 97}


def func3():
    return (12, 98, 46)


def func4():
    return 28

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
