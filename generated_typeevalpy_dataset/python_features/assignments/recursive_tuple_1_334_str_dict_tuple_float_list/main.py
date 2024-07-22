# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'hkctp'


def func2():
    return {'wywvm': 35, 'sezjq': 51, 'dmbte': 87}


def func3():
    return (25, 45, 32)


def func4():
    return 70.08


def func5():
    return [61, 70, 51]


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
