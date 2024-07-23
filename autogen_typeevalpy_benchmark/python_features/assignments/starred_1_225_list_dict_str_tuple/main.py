# Functions are assigned to variables via starred assignment
def func1():
    return [64, 14, 10]


def func2():
    return {'xxvfd': 61, 'awxei': 64, 'iqpjk': 2}


def func3():
    return 'hlkbn'


def func4():
    return (8, 91, 27)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
