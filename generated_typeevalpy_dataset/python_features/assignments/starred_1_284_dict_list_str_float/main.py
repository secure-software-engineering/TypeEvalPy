# Functions are assigned to variables via starred assignment
def func1():
    return {'zywcr': 24, 'uaiag': 79, 'pwbho': 98}


def func2():
    return [44, 70, 74]


def func3():
    return 'ttoxq'


def func4():
    return 48.48

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
