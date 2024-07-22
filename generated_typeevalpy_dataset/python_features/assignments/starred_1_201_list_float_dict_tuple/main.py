# Functions are assigned to variables via starred assignment
def func1():
    return [98, 17, 46]


def func2():
    return 44.23


def func3():
    return {'sgjsa': 87, 'gdodt': 42, 'uvkgy': 17}


def func4():
    return (3, 4, 66)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
