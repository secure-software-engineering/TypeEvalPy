# Functions are assigned to variables via starred assignment
def func1():
    return 89.1


def func2():
    return [21, 49, 40]


def func3():
    return {'oukci': 90, 'gczhf': 80, 'nxiia': 57}


def func4():
    return (20, 91, 42)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
