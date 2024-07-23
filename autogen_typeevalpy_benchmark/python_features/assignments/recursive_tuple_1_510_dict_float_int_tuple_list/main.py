# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'grsdk': 57, 'eiskt': 32, 'lwbyj': 42}


def func2():
    return 29.6


def func3():
    return 32


def func4():
    return (35, 52, 22)


def func5():
    return [92, 95, 88]


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
