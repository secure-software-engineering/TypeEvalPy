# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 67


def func2():
    return 88.14


def func3():
    return 'xoqgm'


def func4():
    return [34, 79, 76]


def func5():
    return (31, 3, 49)


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
