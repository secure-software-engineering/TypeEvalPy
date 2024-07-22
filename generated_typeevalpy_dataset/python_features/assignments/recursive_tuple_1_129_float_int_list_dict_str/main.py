# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 25.07


def func2():
    return 66


def func3():
    return [88, 92, 27]


def func4():
    return {'pnlkx': 31, 'gkqdu': 63, 'koggo': 52}


def func5():
    return 'kmrls'


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
