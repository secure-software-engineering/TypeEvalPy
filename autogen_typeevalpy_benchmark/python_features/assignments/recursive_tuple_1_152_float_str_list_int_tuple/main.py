# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 49.13


def func2():
    return 'cxvnh'


def func3():
    return [71, 27, 16]


def func4():
    return 48


def func5():
    return (93, 19, 5)


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
