# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 35.6


def func2():
    return [92, 24, 39]


def func3():
    return (80, 56, 37)


def func4():
    return 'bmlxh'


def func5():
    return {'cgcjh': 7, 'vhcxp': 2, 'bmniy': 35}


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
