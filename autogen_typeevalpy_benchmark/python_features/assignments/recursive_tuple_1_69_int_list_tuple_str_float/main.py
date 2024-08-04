# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 16


def func2():
    return [31, 51, 63]


def func3():
    return (39, 89, 77)


def func4():
    return 'yqjru'


def func5():
    return 66.19


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
