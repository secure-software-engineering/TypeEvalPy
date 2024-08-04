# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'cjewq': 99, 'tvmfj': 36, 'dultz': 55}


def func2():
    return [99, 60, 60]


def func3():
    return (19, 5, 46)


def func4():
    return 7.4


def func5():
    return 'clbnd'


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
