# Functions are assigned to variables via starred assignment
def func1():
    return {'wdfnw': 84, 'vduef': 60, 'yjqly': 38}


def func2():
    return 75.53


def func3():
    return [24, 53, 53]


def func4():
    return (80, 92, 60)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
