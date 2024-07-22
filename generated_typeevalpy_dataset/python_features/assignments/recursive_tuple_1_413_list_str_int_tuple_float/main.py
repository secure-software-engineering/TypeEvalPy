# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [79, 87, 76]


def func2():
    return 'bfwyr'


def func3():
    return 59


def func4():
    return (32, 31, 11)


def func5():
    return 86.08


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
