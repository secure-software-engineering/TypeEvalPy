# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (50, 47, 29)


def func2():
    return [11, 94, 10]


def func3():
    return {'piqcs': 6, 'rfmul': 23, 'omahi': 96}


def func4():
    return 32


def func5():
    return 27.95


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
