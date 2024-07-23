# Functions are assigned to variables via starred assignment
def func1():
    return [12, 44, 33]


def func2():
    return 27


def func3():
    return (35, 74, 9)


def func4():
    return {'bzaoj': 7, 'psiww': 88, 'xqmvu': 23}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
