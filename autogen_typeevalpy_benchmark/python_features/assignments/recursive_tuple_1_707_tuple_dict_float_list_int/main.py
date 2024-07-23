# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (67, 1, 48)


def func2():
    return {'rebcz': 7, 'zmgtc': 59, 'bquoq': 39}


def func3():
    return 6.27


def func4():
    return [3, 53, 14]


def func5():
    return 11


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
