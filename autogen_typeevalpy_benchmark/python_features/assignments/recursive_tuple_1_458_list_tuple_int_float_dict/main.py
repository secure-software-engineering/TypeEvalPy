# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [51, 37, 87]


def func2():
    return (80, 28, 39)


def func3():
    return 99


def func4():
    return 72.42


def func5():
    return {'fxdhd': 29, 'afbpz': 84, 'hbhpc': 44}


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
