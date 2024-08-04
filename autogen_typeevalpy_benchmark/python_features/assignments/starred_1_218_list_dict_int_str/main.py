# Functions are assigned to variables via starred assignment
def func1():
    return [3, 63, 89]


def func2():
    return {'zhloz': 19, 'kzkkn': 44, 'mfcpj': 20}


def func3():
    return 58


def func4():
    return 'uqbeg'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
