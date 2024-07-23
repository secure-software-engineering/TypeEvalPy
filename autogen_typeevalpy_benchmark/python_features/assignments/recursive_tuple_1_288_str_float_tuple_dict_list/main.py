# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'wqrxp'


def func2():
    return 36.21


def func3():
    return (48, 53, 52)


def func4():
    return {'dcjrm': 86, 'pfcwi': 58, 'vzoyz': 28}


def func5():
    return [72, 53, 60]


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
