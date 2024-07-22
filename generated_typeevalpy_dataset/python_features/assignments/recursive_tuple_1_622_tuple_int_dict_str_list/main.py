# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (88, 34, 77)


def func2():
    return 85


def func3():
    return {'bchtz': 34, 'utxgb': 28, 'rdpgr': 98}


def func4():
    return 'itcdc'


def func5():
    return [68, 7, 47]


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
