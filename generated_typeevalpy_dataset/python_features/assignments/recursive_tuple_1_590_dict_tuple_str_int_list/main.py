# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'fgfbu': 30, 'uxbmn': 79, 'qpkgc': 84}


def func2():
    return (20, 59, 28)


def func3():
    return 'mxjqh'


def func4():
    return 65


def func5():
    return [51, 31, 5]


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
