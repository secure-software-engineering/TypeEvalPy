# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 60


def func2():
    return 13.98


def func3():
    return 'hsyvr'


def func4():
    return [95, 47, 61]


def func5():
    return (21, 80, 27)


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
