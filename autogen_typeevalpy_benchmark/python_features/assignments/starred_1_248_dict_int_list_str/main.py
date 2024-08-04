# Functions are assigned to variables via starred assignment
def func1():
    return {'jxoda': 63, 'dblah': 79, 'ogrls': 90}


def func2():
    return 56


def func3():
    return [98, 27, 81]


def func4():
    return 'kbqsj'

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
