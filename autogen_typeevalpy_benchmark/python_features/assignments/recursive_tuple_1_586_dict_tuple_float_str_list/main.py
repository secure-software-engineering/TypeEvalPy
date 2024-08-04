# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'uqtgw': 30, 'hgxpd': 16, 'vaotz': 17}


def func2():
    return (35, 97, 35)


def func3():
    return 9.96


def func4():
    return 'wbutk'


def func5():
    return [79, 77, 79]


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
