# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 49.09


def func2():
    return 48


def func3():
    return [31, 50, 11]


def func4():
    return {'gobip': 61, 'zhmlb': 15, 'crjie': 88}


def func5():
    return 'sxank'


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
