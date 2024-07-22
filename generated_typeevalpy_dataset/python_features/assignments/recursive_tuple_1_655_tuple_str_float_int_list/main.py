# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (82, 38, 56)


def func2():
    return 'zcxro'


def func3():
    return 95.44


def func4():
    return 23


def func5():
    return [65, 63, 64]


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
