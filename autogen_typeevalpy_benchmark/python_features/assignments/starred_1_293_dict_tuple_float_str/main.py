# Functions are assigned to variables via starred assignment
def func1():
    return {'nhyck': 15, 'ejexq': 86, 'rpfom': 90}


def func2():
    return (71, 65, 82)


def func3():
    return 25.35


def func4():
    return 'vpxyx'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
