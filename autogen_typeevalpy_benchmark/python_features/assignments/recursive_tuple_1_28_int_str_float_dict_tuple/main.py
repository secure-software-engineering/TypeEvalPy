# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 85


def func2():
    return 'gbtbv'


def func3():
    return 31.04


def func4():
    return {'yhwom': 62, 'sqrxr': 97, 'yiaea': 18}


def func5():
    return (99, 36, 81)


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
