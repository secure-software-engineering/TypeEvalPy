# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 6


def func2():
    return [84, 5, 19]


def func3():
    return 'qgjon'


def func4():
    return {'nryge': 23, 'gugez': 62, 'lrzby': 93}


def func5():
    return 93.72


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
