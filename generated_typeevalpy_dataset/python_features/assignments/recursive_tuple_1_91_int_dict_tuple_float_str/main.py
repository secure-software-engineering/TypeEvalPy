# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 32


def func2():
    return {'gqvfm': 68, 'sqcps': 64, 'yafpv': 53}


def func3():
    return (27, 17, 59)


def func4():
    return 94.25


def func5():
    return 'vduqv'


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
