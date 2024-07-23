# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'acuiu'


def func2():
    return 38


def func3():
    return [70, 38, 14]


def func4():
    return {'pfpez': 23, 'thpvm': 90, 'xskzi': 12}


def func5():
    return 24.63


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
