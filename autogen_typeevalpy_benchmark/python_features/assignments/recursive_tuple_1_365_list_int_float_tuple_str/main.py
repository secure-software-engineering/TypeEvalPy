# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [68, 58, 100]


def func2():
    return 25


def func3():
    return 34.92


def func4():
    return (31, 62, 86)


def func5():
    return 'xtnkf'


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
