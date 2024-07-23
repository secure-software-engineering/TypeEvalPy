# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (30, 17, 25)


def func2():
    return 39


def func3():
    return 61.07


def func4():
    return {'aqszr': 72, 'zopll': 36, 'pghpi': 82}


def func5():
    return [90, 13, 94]


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
