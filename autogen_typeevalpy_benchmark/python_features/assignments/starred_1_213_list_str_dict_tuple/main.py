# Functions are assigned to variables via starred assignment
def func1():
    return [78, 71, 27]


def func2():
    return 'kxgmo'


def func3():
    return {'yjnkj': 27, 'wimcl': 39, 'jbruv': 32}


def func4():
    return (97, 12, 65)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
