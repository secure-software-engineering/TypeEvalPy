# Functions are assigned to variables via starred assignment
def func1():
    return 19


def func2():
    return 'bvshf'


def func3():
    return {'rmxzj': 87, 'rwrlm': 75, 'tvuxy': 75}


def func4():
    return [81, 61, 14]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
