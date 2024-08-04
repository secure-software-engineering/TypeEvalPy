# Functions are assigned to variables via starred assignment
def func1():
    return 'bcqna'


def func2():
    return 1.8


def func3():
    return {'fxobw': 54, 'wlgun': 3, 'ktcig': 45}


def func4():
    return [32, 75, 20]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
