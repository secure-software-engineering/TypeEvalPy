# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [12, 94, 77]


def func2():
    return {'ozsed': 71, 'fofln': 64, 'gudcq': 4}


def func3():
    return 39.8


def func4():
    return 21


def func5():
    return (73, 27, 23)


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
