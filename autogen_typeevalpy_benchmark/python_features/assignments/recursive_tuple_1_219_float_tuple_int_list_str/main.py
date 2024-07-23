# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 99.99


def func2():
    return (21, 46, 59)


def func3():
    return 50


def func4():
    return [38, 58, 75]


def func5():
    return 'xlzjc'


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
