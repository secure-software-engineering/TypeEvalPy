# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 85


def func2():
    return [57, 12, 35]


def func3():
    return 'sklhn'


def func4():
    return (61, 97, 44)


def func5():
    return 98.58


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
