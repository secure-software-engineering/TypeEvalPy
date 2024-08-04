# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 66


def func2():
    return [91, 63, 82]


def func3():
    return 'rsqyt'


def func4():
    return 24.99


def func5():
    return {'avqrs': 83, 'qglrg': 92, 'pyvau': 50}


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
