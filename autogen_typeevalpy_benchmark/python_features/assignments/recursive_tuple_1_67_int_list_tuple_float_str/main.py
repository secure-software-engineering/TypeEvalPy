# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 94


def func2():
    return [71, 10, 73]


def func3():
    return (62, 40, 14)


def func4():
    return 82.45


def func5():
    return 'zsdhr'


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
