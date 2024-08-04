# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (20, 97, 54)


def func2():
    return 90.28


def func3():
    return [52, 3, 17]


def func4():
    return 'fubna'


def func5():
    return 48


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
