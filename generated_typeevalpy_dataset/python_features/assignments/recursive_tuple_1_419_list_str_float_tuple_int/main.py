# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [10, 17, 11]


def func2():
    return 'zgmrv'


def func3():
    return 92.28


def func4():
    return (67, 42, 94)


def func5():
    return 42


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
