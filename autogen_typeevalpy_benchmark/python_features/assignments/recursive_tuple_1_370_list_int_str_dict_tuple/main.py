# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [66, 96, 17]


def func2():
    return 71


def func3():
    return 'estgr'


def func4():
    return {'psbki': 67, 'nysxo': 54, 'lypov': 61}


def func5():
    return (99, 36, 56)


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
