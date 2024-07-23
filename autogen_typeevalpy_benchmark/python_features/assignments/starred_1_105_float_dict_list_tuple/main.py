# Functions are assigned to variables via starred assignment
def func1():
    return 50.26


def func2():
    return {'wyzid': 72, 'pwceb': 86, 'dlich': 44}


def func3():
    return [80, 82, 9]


def func4():
    return (34, 70, 10)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
