# Functions are assigned to variables via starred assignment
def func1():
    return 21


def func2():
    return 'rfggq'


def func3():
    return {'vcqky': 23, 'twprs': 60, 'jaqyo': 67}


def func4():
    return (41, 15, 28)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
