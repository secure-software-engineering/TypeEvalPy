# Functions are assigned to variables via starred assignment
def func1():
    return (81, 71, 99)


def func2():
    return 49.03


def func3():
    return {'xwqvw': 43, 'hffmd': 35, 'wfhxz': 15}


def func4():
    return 65

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
