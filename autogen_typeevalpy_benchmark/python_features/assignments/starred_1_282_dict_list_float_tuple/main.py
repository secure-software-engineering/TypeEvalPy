# Functions are assigned to variables via starred assignment
def func1():
    return {'nozif': 89, 'egvkn': 69, 'fvlsq': 2}


def func2():
    return [98, 6, 20]


def func3():
    return 15.63


def func4():
    return (54, 34, 20)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
