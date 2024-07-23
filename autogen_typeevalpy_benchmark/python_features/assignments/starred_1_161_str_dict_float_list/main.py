# Functions are assigned to variables via starred assignment
def func1():
    return 'vagsj'


def func2():
    return {'tehkn': 93, 'iznxs': 49, 'wmnvx': 98}


def func3():
    return 10.62


def func4():
    return [17, 41, 55]

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
