# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'ifqrl': 13, 'ammko': 30, 'rippi': 69}


def func2():
    return 23.3


def func3():
    return (1, 63, 11)


def func4():
    return 'zhsfe'


def func5():
    return [77, 8, 1]


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
