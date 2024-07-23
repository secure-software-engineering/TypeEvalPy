# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'ezzfj'


def func2():
    return 14


def func3():
    return [53, 4, 21]


def func4():
    return 22.38


def func5():
    return (76, 48, 61)


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
