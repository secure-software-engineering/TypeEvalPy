# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 29


def func2():
    return 'lbtqr'


def func3():
    return (77, 86, 69)


def func4():
    return 44.23


def func5():
    return [11, 72, 51]


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
