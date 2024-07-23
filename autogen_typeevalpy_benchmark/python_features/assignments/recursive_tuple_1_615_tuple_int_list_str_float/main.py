# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (3, 64, 38)


def func2():
    return 20


def func3():
    return [77, 11, 96]


def func4():
    return 'zkvid'


def func5():
    return 24.08


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
