# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (68, 87, 70)


def func2():
    return 34.06


def func3():
    return 'lsjdw'


def func4():
    return [57, 56, 76]


def func5():
    return {'mtrkp': 65, 'zbuqb': 91, 'xvyxm': 78}


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
