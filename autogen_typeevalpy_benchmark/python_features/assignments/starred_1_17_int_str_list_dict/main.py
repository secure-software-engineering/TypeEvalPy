# Functions are assigned to variables via starred assignment
def func1():
    return 55


def func2():
    return 'yyqao'


def func3():
    return [43, 3, 85]


def func4():
    return {'zsqda': 81, 'dgfhh': 17, 'egvyi': 16}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
