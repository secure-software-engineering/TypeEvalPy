# Functions are assigned to variables via starred assignment
def func1():
    return (75, 42, 45)


def func2():
    return {'mnbvt': 20, 'euemo': 37, 'fsash': 52}


def func3():
    return [20, 3, 10]


def func4():
    return 87

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
