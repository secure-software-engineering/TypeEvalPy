# Functions are assigned to variables via starred assignment
def func1():
    return 91.33


def func2():
    return (4, 32, 42)


def func3():
    return 'spbpn'


def func4():
    return {'edxmp': 56, 'guucm': 85, 'rxcof': 58}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
