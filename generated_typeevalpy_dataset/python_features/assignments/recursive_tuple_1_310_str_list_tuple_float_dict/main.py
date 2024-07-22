# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'nxyrj'


def func2():
    return [5, 20, 39]


def func3():
    return (55, 7, 10)


def func4():
    return 44.12


def func5():
    return {'fnafe': 21, 'cclfy': 28, 'dzbwg': 75}


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
