# Functions are assigned to variables via starred assignment
def func1():
    return 61.91


def func2():
    return 34


def func3():
    return {'kindv': 31, 'ghklj': 13, 'svvnb': 4}


def func4():
    return 'wyzeh'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
