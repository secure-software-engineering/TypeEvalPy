# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 39


def func2():
    return (17, 31, 88)


def func3():
    return [1, 71, 85]


def func4():
    return 'vgcaq'


def func5():
    return {'vakxb': 10, 'hcorc': 100, 'dhhxc': 5}


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
