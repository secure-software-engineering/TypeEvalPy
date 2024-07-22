# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 56


def func2():
    return 'nwibo'


def func3():
    return 9.0


def func4():
    return [63, 29, 64]


def func5():
    return (84, 80, 95)


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
