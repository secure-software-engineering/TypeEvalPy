# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (78, 96, 11)


def func2():
    return 47.89


def func3():
    return [33, 40, 11]


def func4():
    return {'dxisc': 86, 'eqxwc': 58, 'qyalk': 78}


def func5():
    return 9


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
