# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [60, 42, 34]


def func2():
    return 74.94


def func3():
    return {'jqmjw': 51, 'yiqnu': 7, 'rlxos': 71}


def func4():
    return 24


def func5():
    return 'syqel'


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
