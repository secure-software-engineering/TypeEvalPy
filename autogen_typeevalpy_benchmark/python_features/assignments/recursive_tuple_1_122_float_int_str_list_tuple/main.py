# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 54.52


def func2():
    return 4


def func3():
    return 'okyct'


def func4():
    return [80, 87, 52]


def func5():
    return (55, 59, 47)


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
