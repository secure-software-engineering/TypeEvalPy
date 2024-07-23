# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 64


def func2():
    return {'ngywr': 62, 'klxsn': 78, 'bafgo': 93}


def func3():
    return (23, 68, 88)


def func4():
    return 'lxaew'


def func5():
    return 14.47


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
