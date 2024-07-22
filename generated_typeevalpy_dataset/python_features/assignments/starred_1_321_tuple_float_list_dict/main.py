# Functions are assigned to variables via starred assignment
def func1():
    return (75, 86, 19)


def func2():
    return 89.63


def func3():
    return [99, 82, 98]


def func4():
    return {'ehlmn': 86, 'dvvqq': 93, 'bwebl': 45}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
