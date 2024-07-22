# Functions are assigned to variables via starred assignment
def func1():
    return 'sdnpn'


def func2():
    return {'wibtq': 43, 'qxijk': 41, 'obezk': 84}


def func3():
    return 59


def func4():
    return (28, 84, 31)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
