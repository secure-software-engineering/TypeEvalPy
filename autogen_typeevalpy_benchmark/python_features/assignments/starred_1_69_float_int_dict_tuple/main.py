# Functions are assigned to variables via starred assignment
def func1():
    return 75.0


def func2():
    return 6


def func3():
    return {'edryt': 88, 'hjbhk': 15, 'jmffh': 10}


def func4():
    return (59, 54, 100)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
