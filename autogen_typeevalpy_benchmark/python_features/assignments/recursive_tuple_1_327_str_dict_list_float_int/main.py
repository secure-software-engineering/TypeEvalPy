# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'phzlh'


def func2():
    return {'apzbv': 30, 'kmwoy': 86, 'vfgxw': 75}


def func3():
    return [33, 51, 34]


def func4():
    return 1.42


def func5():
    return 30


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
