# Functions are assigned to variables via starred assignment
def func1():
    return 90


def func2():
    return {'qgfmy': 97, 'mfkyw': 39, 'nlvqf': 63}


def func3():
    return [49, 76, 72]


def func4():
    return 92.6

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
