# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 92.26


def func2():
    return 'zopym'


def func3():
    return (88, 21, 56)


def func4():
    return 56


def func5():
    return [16, 86, 77]


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
