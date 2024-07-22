# Functions are assigned to variables via starred assignment
def func1():
    return {'wsvmb': 56, 'nzvyb': 81, 'lkwuz': 7}


def func2():
    return [69, 94, 83]


def func3():
    return 'ieyhx'


def func4():
    return (25, 10, 50)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
