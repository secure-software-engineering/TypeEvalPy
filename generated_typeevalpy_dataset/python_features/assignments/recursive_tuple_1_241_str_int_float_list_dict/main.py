# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'irivt'


def func2():
    return 14


def func3():
    return 85.72


def func4():
    return [28, 68, 4]


def func5():
    return {'cihgn': 17, 'fsrgc': 17, 'rmfmv': 83}


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
