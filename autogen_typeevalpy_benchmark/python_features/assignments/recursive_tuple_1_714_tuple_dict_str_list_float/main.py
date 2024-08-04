# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (66, 95, 48)


def func2():
    return {'jpalz': 81, 'vdaui': 60, 'uftck': 60}


def func3():
    return 'xnbih'


def func4():
    return [94, 37, 32]


def func5():
    return 44.95


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
