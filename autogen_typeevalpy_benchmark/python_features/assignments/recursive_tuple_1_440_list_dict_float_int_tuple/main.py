# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [16, 36, 22]


def func2():
    return {'wihdr': 39, 'zjktg': 40, 'lnxpw': 3}


def func3():
    return 16.59


def func4():
    return 56


def func5():
    return (32, 68, 60)


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
