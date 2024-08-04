# Functions are assigned to variables via starred assignment
def func1():
    return (16, 51, 4)


def func2():
    return 26


def func3():
    return {'rynbq': 74, 'wttix': 79, 'tzzyt': 49}


def func4():
    return 'wflwa'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
