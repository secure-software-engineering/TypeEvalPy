# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 64


def func2():
    return 'ktdjt'


def func3():
    return (65, 99, 100)


def func4():
    return 33.28


def func5():
    return [58, 22, 33]


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
