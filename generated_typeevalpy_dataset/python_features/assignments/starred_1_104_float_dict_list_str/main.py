# Functions are assigned to variables via starred assignment
def func1():
    return 71.78


def func2():
    return {'ldhah': 10, 'qxpkr': 57, 'ggxzn': 77}


def func3():
    return [91, 20, 90]


def func4():
    return 'mbofj'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
