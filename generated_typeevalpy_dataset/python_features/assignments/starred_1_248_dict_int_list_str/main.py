# Functions are assigned to variables via starred assignment
def func1():
    return {'sevxk': 10, 'dhmev': 19, 'ippvi': 3}


def func2():
    return 59


def func3():
    return [75, 40, 46]


def func4():
    return 'logsv'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
