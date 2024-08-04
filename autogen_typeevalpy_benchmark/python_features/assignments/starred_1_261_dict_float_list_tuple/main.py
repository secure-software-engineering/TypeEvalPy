# Functions are assigned to variables via starred assignment
def func1():
    return {'yhgtv': 43, 'zckyt': 81, 'gpxfp': 82}


def func2():
    return 71.35


def func3():
    return [73, 95, 7]


def func4():
    return (60, 78, 91)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
