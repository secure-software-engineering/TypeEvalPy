# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'vofuv': 71, 'hldxs': 72, 'zhmsc': 63}


def func2():
    return 38


def func3():
    return (100, 88, 20)


def func4():
    return 7.62


def func5():
    return 'thdaj'


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
