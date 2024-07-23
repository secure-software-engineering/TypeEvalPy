# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [63, 52, 17]


def func2():
    return 'uyvwk'


def func3():
    return 63.54


def func4():
    return {'lmipk': 59, 'oaxlg': 58, 'mddso': 38}


def func5():
    return (51, 1, 17)


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
