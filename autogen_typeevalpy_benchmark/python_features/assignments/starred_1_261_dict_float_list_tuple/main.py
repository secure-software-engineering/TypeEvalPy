# Functions are assigned to variables via starred assignment
def func1():
    return {'riwqx': 62, 'hypaq': 40, 'ymflb': 36}


def func2():
    return 87.26


def func3():
    return [58, 30, 100]


def func4():
    return (75, 73, 42)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
