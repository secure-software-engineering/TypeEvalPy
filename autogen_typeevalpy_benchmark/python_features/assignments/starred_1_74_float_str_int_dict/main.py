# Functions are assigned to variables via starred assignment
def func1():
    return 93.57


def func2():
    return 'jphbg'


def func3():
    return 49


def func4():
    return {'trpcl': 7, 'demna': 62, 'nlpzk': 43}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
