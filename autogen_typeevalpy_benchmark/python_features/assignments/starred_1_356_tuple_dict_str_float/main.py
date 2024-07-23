# Functions are assigned to variables via starred assignment
def func1():
    return (42, 38, 67)


def func2():
    return {'elblw': 58, 'vnlxt': 72, 'wyqol': 98}


def func3():
    return 'akuzv'


def func4():
    return 50.33

a, *b, c = func1, func2, func3, func4

d = a()
e = b[0]()
f = b[1]()
g = c()
