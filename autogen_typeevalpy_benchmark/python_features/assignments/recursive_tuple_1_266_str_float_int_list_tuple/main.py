# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'zmqpz'


def func2():
    return 37.16


def func3():
    return 33


def func4():
    return [25, 66, 36]


def func5():
    return (67, 4, 63)


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
