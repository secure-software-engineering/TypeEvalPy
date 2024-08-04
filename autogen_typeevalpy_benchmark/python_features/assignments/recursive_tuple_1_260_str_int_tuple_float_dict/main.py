# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'htzkg'


def func2():
    return 21


def func3():
    return (48, 95, 3)


def func4():
    return 43.74


def func5():
    return {'hbkww': 44, 'zdqfk': 42, 'wllym': 86}


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
