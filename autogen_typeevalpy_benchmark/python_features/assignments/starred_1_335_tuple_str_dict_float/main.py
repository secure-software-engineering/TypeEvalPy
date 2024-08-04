# Functions are assigned to variables via starred assignment
def func1():
    return (81, 19, 44)


def func2():
    return 'giccq'


def func3():
    return {'uvoee': 71, 'mzbkk': 28, 'sdlxv': 74}


def func4():
    return 65.01

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
