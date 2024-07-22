# Functions are assigned to variables via starred assignment
def func1():
    return (93, 24, 74)


def func2():
    return {'wrwfc': 82, 'qysco': 77, 'ozgke': 17}


def func3():
    return [72, 97, 27]


def func4():
    return 'pvxyy'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
