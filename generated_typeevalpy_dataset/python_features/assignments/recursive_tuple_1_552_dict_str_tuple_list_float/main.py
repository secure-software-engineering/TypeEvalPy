# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'insdu': 6, 'xlwgx': 35, 'rrikg': 22}


def func2():
    return 'chwiy'


def func3():
    return (5, 12, 40)


def func4():
    return [36, 11, 35]


def func5():
    return 31.45


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
