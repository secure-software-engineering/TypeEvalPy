# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 88


def func2():
    return [85, 61, 66]


def func3():
    return {'kezyv': 55, 'ajbui': 61, 'lpkpc': 85}


def func4():
    return 85.85


def func5():
    return 'xthfd'


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
