# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'qctlr'


def func2():
    return (44, 4, 5)


def func3():
    return [98, 2, 100]


def func4():
    return 3.7


def func5():
    return 86


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
