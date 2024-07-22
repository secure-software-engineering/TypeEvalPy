# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [60, 37, 98]


def func2():
    return (91, 85, 63)


def func3():
    return 40.39


def func4():
    return 11


def func5():
    return 'sggvb'


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
