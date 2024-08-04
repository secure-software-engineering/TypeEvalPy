# Functions are assigned to variables via starred assignment
def func1():
    return 49


def func2():
    return 'jpjku'


def func3():
    return {'kbprn': 49, 'ghgas': 88, 'dyvyz': 92}


def func4():
    return (47, 26, 100)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
