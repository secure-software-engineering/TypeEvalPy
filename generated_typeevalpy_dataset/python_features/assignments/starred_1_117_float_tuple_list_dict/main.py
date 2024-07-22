# Functions are assigned to variables via starred assignment
def func1():
    return 34.1


def func2():
    return (73, 36, 25)


def func3():
    return [82, 33, 58]


def func4():
    return {'gfleu': 58, 'ufhcj': 47, 'fyuvn': 24}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
