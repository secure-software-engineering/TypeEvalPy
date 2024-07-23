# Functions are assigned to variables via starred assignment
def func1():
    return {'kubtp': 86, 'gyfjv': 74, 'zdltz': 48}


def func2():
    return (8, 41, 87)


def func3():
    return 'dnktc'


def func4():
    return 48.44

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
