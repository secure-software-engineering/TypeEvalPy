# Functions are assigned to variables via starred assignment
def func1():
    return 2


def func2():
    return 'qtfwv'


def func3():
    return {'yumxy': 8, 'dwndd': 2, 'tqxfu': 57}


def func4():
    return 90.83

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
