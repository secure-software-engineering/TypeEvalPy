# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 32


def func2():
    return [56, 98, 43]


def func3():
    return {'bhwlk': 98, 'ymomy': 48, 'keado': 19}


def func4():
    return 'xncky'


def func5():
    return 21.9


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
