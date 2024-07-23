# Functions are assigned to variables via starred assignment
def func1():
    return {'dahkc': 15, 'voapz': 56, 'dlusy': 25}


def func2():
    return 'tpurc'


def func3():
    return [47, 78, 94]


def func4():
    return (34, 37, 83)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
