# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'pkvqx'


def func2():
    return (59, 86, 34)


def func3():
    return 86


def func4():
    return 70.11


def func5():
    return [58, 61, 87]


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
