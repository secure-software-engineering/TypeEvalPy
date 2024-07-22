# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'azcny': 33, 'fvnkp': 43, 'nvqlq': 34}


def func2():
    return (50, 30, 66)


def func3():
    return 89.16


def func4():
    return 'aivdp'


def func5():
    return [6, 47, 78]


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
