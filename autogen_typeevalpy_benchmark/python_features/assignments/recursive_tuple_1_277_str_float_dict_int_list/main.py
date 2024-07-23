# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'etrkw'


def func2():
    return 53.64


def func3():
    return {'lwxoi': 13, 'meucc': 57, 'zojax': 62}


def func4():
    return 72


def func5():
    return [61, 100, 23]


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
