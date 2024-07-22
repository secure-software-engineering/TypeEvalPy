# Functions are assigned to variables via starred assignment
def func1():
    return 65


def func2():
    return 47.34


def func3():
    return {'ukxtl': 40, 'ujxuz': 71, 'fyhks': 12}


def func4():
    return (41, 45, 12)

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
