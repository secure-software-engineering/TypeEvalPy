# Functions are assigned to variables via starred assignment
def func1():
    return [91, 31, 88]


def func2():
    return {'kwhak': 61, 'sxtgb': 7, 'dvkls': 92}


def func3():
    return 'jmjff'


def func4():
    return (88, 15, 71)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
