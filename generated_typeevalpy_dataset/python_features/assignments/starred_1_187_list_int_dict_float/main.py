# Functions are assigned to variables via starred assignment
def func1():
    return [1, 16, 39]


def func2():
    return 73


def func3():
    return {'ykhyn': 31, 'jnsls': 91, 'uaewj': 18}


def func4():
    return 53.49

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
