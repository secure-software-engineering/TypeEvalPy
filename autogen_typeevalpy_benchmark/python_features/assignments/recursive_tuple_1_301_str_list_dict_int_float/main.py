# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'sxodk'


def func2():
    return [76, 2, 26]


def func3():
    return {'mjzjd': 87, 'krwea': 70, 'scsdu': 87}


def func4():
    return 4


def func5():
    return 14.31


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
