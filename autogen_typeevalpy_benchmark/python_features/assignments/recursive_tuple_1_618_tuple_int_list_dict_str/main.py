# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (75, 8, 74)


def func2():
    return 29


def func3():
    return [31, 28, 40]


def func4():
    return {'cjaft': 92, 'gbfay': 74, 'pandv': 89}


def func5():
    return 'pucxp'


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
