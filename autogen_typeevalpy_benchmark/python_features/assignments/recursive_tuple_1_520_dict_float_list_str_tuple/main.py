# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'wrqsa': 14, 'nrxuo': 99, 'nubqb': 43}


def func2():
    return 22.33


def func3():
    return [21, 63, 42]


def func4():
    return 'abbck'


def func5():
    return (48, 98, 52)


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
