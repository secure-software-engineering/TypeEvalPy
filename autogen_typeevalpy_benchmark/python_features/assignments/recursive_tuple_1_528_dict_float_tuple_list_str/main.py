# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'ephrj': 82, 'sikzi': 7, 'jcbib': 47}


def func2():
    return 31.54


def func3():
    return (12, 34, 58)


def func4():
    return [59, 40, 35]


def func5():
    return 'mtqjd'


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
