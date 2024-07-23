# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 60.47


def func2():
    return (3, 60, 56)


def func3():
    return 20


def func4():
    return {'swhtq': 69, 'udwrg': 51, 'jxcnc': 11}


def func5():
    return [27, 6, 2]


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
