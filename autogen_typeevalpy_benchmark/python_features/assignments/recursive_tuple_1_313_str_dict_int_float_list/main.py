# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'tnanb'


def func2():
    return {'dbedw': 49, 'vohge': 18, 'cgqtb': 1}


def func3():
    return 37


def func4():
    return 46.62


def func5():
    return [63, 87, 97]


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
