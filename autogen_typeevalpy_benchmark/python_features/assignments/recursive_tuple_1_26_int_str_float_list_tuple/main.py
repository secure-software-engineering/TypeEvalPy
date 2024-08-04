# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 4


def func2():
    return 'pqigc'


def func3():
    return 24.6


def func4():
    return [44, 7, 43]


def func5():
    return (67, 31, 10)


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
