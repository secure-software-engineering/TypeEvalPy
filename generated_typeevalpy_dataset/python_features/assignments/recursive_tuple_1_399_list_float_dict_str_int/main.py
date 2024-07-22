# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [23, 89, 55]


def func2():
    return 76.56


def func3():
    return {'kqebh': 23, 'yfbbu': 89, 'vzaub': 33}


def func4():
    return 'lmfeu'


def func5():
    return 31


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
