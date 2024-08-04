# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'nzkwa': 24, 'wvzee': 32, 'wirhu': 4}


def func2():
    return [16, 91, 52]


def func3():
    return 'bpylv'


def func4():
    return 31


def func5():
    return 50.17


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
