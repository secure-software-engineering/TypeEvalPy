# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (18, 82, 26)


def func2():
    return 8.91


def func3():
    return 'thtvo'


def func4():
    return [94, 32, 74]


def func5():
    return 35


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
