# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (52, 88, 33)


def func2():
    return 'ctwof'


def func3():
    return 3


def func4():
    return [64, 97, 47]


def func5():
    return 93.09


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
