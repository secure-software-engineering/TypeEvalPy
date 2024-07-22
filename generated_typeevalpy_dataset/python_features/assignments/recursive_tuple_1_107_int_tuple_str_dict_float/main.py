# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 90


def func2():
    return (88, 77, 43)


def func3():
    return 'pfekz'


def func4():
    return {'qgftu': 23, 'msxla': 27, 'tzryb': 40}


def func5():
    return 52.4


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
