# Functions are assigned to variables via starred assignment
def func1():
    return {'ustnf': 10, 'ihrja': 96, 'yygsz': 89}


def func2():
    return 17.89


def func3():
    return (43, 29, 38)


def func4():
    return [42, 55, 40]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
