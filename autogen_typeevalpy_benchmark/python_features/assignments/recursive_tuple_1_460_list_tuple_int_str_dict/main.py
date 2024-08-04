# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [5, 8, 53]


def func2():
    return (63, 73, 74)


def func3():
    return 2


def func4():
    return 'qklxv'


def func5():
    return {'bosmb': 75, 'sgmgr': 90, 'syroh': 48}


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
