# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'bqgxm'


def func2():
    return (98, 60, 38)


def func3():
    return 59.52


def func4():
    return 66


def func5():
    return {'hcsms': 59, 'zzmmt': 50, 'ibqhh': 63}


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
