# Functions are assigned to variables via starred assignment
def func1():
    return (48, 15, 95)


def func2():
    return {'tomiq': 26, 'odafi': 1, 'wpchj': 15}


def func3():
    return 65.85


def func4():
    return [43, 53, 27]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
