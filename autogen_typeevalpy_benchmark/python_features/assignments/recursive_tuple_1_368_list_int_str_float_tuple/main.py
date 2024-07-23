# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [80, 35, 96]


def func2():
    return 2


def func3():
    return 'gtjos'


def func4():
    return 85.93


def func5():
    return (64, 68, 90)


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
