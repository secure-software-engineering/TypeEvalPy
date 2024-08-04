# Functions are assigned to variables via starred assignment
def func1():
    return 'yurom'


def func2():
    return (68, 100, 62)


def func3():
    return {'exmvs': 15, 'geijk': 55, 'ocxpi': 2}


def func4():
    return [31, 25, 98]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
