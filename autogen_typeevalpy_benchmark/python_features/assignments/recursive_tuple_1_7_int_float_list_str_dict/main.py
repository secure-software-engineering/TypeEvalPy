# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 8


def func2():
    return 62.16


def func3():
    return [15, 15, 43]


def func4():
    return 'ztshm'


def func5():
    return {'podfi': 75, 'hjazu': 1, 'qfhtk': 87}


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
