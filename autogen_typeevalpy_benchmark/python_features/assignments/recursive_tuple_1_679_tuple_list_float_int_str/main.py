# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (57, 49, 34)


def func2():
    return [12, 39, 78]


def func3():
    return 5.45


def func4():
    return 28


def func5():
    return 'yzxoa'


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
