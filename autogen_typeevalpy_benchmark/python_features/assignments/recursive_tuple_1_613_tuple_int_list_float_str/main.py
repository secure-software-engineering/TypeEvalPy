# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (97, 12, 69)


def func2():
    return 57


def func3():
    return [8, 92, 85]


def func4():
    return 48.03


def func5():
    return 'fxxtq'


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
