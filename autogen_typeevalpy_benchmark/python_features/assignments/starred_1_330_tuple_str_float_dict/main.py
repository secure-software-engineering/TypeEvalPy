# Functions are assigned to variables via starred assignment
def func1():
    return (90, 42, 25)


def func2():
    return 'oeqkk'


def func3():
    return 83.26


def func4():
    return {'amhxw': 65, 'dszit': 25, 'phwrt': 94}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
