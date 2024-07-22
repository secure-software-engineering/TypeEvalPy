# Functions are assigned to variables via starred assignment
def func1():
    return 'mkege'


def func2():
    return (18, 46, 38)


def func3():
    return [26, 64, 2]


def func4():
    return {'yfzsp': 35, 'ehidz': 85, 'jllbl': 55}

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
