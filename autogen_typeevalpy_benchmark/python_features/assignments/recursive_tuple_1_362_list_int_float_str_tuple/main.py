# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [11, 81, 59]


def func2():
    return 93


def func3():
    return 22.13


def func4():
    return 'mtoka'


def func5():
    return (36, 9, 83)


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
