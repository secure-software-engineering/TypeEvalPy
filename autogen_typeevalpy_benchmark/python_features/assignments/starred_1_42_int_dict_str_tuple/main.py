# Functions are assigned to variables via starred assignment
def func1():
    return 7


def func2():
    return {'ycgls': 53, 'fpgqg': 70, 'asafq': 74}


def func3():
    return 'atopa'


def func4():
    return (54, 61, 82)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
