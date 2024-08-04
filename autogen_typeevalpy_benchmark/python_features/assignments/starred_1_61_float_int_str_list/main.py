# Functions are assigned to variables via starred assignment
def func1():
    return 27.95


def func2():
    return 78


def func3():
    return 'uuhrl'


def func4():
    return [45, 39, 81]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
