# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (34, 91, 57)


def func2():
    return [37, 45, 16]


def func3():
    return 'tmwjs'


def func4():
    return 64


def func5():
    return 97.91


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
