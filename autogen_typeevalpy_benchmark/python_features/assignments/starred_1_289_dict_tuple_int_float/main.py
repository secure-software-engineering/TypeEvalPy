# Functions are assigned to variables via starred assignment
def func1():
    return {'shnaq': 41, 'onibe': 79, 'rsjpx': 35}


def func2():
    return (50, 76, 92)


def func3():
    return 78


def func4():
    return 53.07

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
