# Functions are assigned to variables via starred assignment
def func1():
    return 'izkla'


def func2():
    return (83, 45, 27)


def func3():
    return {'ezsez': 97, 'rslpn': 23, 'vnecg': 95}


def func4():
    return [19, 58, 53]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
