# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 71.79


def func2():
    return [61, 2, 41]


def func3():
    return 'kdbzi'


def func4():
    return (25, 26, 89)


def func5():
    return 13


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
