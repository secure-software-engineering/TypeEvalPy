# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 15


def func2():
    return 89.42


def func3():
    return [39, 29, 76]


def func4():
    return (70, 53, 75)


def func5():
    return 'fnkqr'


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
