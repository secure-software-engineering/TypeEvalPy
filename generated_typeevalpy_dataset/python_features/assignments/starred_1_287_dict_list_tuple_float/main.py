# Functions are assigned to variables via starred assignment
def func1():
    return {'qzmmv': 90, 'jrfrw': 11, 'egkyx': 57}


def func2():
    return [4, 29, 43]


def func3():
    return (85, 35, 6)


def func4():
    return 34.97

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
