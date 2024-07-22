# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (59, 13, 53)


def func2():
    return [15, 48, 62]


def func3():
    return 85.54


def func4():
    return 38


def func5():
    return 'fwvec'


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
