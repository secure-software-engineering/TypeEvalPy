# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (13, 46, 29)


def func2():
    return [87, 65, 11]


def func3():
    return {'cxnfm': 69, 'aaumj': 79, 'mevac': 55}


def func4():
    return 62


def func5():
    return 'yxaxk'


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
