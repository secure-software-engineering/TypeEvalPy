# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [85, 15, 29]


def func2():
    return 'vkkbn'


def func3():
    return 35.11


def func4():
    return {'dmmqj': 6, 'nmulh': 31, 'dhkfg': 22}


def func5():
    return 62


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
