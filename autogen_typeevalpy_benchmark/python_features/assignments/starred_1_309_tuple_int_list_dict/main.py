# Functions are assigned to variables via starred assignment
def func1():
    return (29, 18, 20)


def func2():
    return 91


def func3():
    return [26, 88, 21]


def func4():
    return {'bnmuj': 26, 'aibwh': 100, 'itskf': 12}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
