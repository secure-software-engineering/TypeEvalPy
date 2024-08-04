# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (55, 51, 38)


def func2():
    return {'elufx': 51, 'bdehy': 41, 'fvgyj': 97}


def func3():
    return [50, 79, 61]


def func4():
    return 'zglhl'


def func5():
    return 22


def func6():
    pass


a, (b, c) = func1, (func2, func3)
i = a()
j = b()
k = c()

a, (b, (c, d)) = func1, (func2, (func3, func4))

h = d()

f, b = c, e = func5, func6

l = e()
m = f()
