# Functions are assigned to variables via starred assignment
def func1():
    return 44


def func2():
    return {'dhasr': 87, 'vlgek': 13, 'gfcer': 100}


def func3():
    return 7.43


def func4():
    return 'tbwey'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
