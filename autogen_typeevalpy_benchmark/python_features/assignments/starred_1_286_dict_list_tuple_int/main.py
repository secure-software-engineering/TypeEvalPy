# Functions are assigned to variables via starred assignment
def func1():
    return {'xnadh': 53, 'zhhpk': 71, 'ujdxz': 52}


def func2():
    return [18, 91, 17]


def func3():
    return (90, 31, 8)


def func4():
    return 60

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
