# Functions are assigned to variables via starred assignment
def func1():
    return 54.83


def func2():
    return (7, 53, 62)


def func3():
    return {'jhktf': 13, 'lsovd': 19, 'gsiwh': 92}


def func4():
    return 73

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
