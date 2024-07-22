# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 4.16


def func2():
    return (51, 42, 6)


def func3():
    return 100


def func4():
    return 'gcmyh'


def func5():
    return [64, 60, 26]


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
