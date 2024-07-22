# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (42, 31, 17)


def func2():
    return 46.17


def func3():
    return {'qgbcz': 8, 'xhwgv': 32, 'jvioq': 14}


def func4():
    return [19, 78, 98]


def func5():
    return 26


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
