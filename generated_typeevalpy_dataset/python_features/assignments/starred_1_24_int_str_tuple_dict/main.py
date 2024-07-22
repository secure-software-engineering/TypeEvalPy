# Functions are assigned to variables via starred assignment
def func1():
    return 40


def func2():
    return 'nufwk'


def func3():
    return (90, 76, 32)


def func4():
    return {'ffsgc': 17, 'yarmb': 33, 'mvnlv': 45}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
