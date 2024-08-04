# Functions are assigned to variables via starred assignment
def func1():
    return 47


def func2():
    return {'zaegm': 95, 'talhx': 63, 'ttosl': 19}


def func3():
    return [76, 41, 35]


def func4():
    return (82, 45, 86)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
