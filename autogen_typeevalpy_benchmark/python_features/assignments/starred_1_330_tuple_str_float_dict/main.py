# Functions are assigned to variables via starred assignment
def func1():
    return (44, 58, 52)


def func2():
    return 'ytgww'


def func3():
    return 78.04


def func4():
    return {'yhhsw': 26, 'esqxg': 82, 'suuxx': 28}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
