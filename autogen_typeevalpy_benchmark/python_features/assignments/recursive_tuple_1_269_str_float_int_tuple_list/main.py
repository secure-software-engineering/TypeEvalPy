# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'zpqqj'


def func2():
    return 53.04


def func3():
    return 63


def func4():
    return (31, 23, 1)


def func5():
    return [33, 57, 74]


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
