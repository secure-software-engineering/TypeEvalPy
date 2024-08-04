# Functions are assigned to variables via starred assignment
def func1():
    return (13, 76, 68)


def func2():
    return [91, 83, 81]


def func3():
    return {'jyrmk': 13, 'roxqk': 48, 'jshsr': 63}


def func4():
    return 66.9

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
