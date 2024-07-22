# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 12


def func2():
    return [47, 1, 23]


def func3():
    return 82.29


def func4():
    return {'bdjmt': 95, 'cphxy': 56, 'bleqx': 60}


def func5():
    return 'lahdk'


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
