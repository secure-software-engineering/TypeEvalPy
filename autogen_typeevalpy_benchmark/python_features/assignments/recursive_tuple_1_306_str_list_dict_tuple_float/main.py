# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'apmgh'


def func2():
    return [65, 36, 52]


def func3():
    return {'cksuo': 55, 'bmxnm': 19, 'laltd': 62}


def func4():
    return (74, 90, 26)


def func5():
    return 65.94


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
