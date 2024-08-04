# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'kogdh'


def func2():
    return (30, 42, 48)


def func3():
    return [85, 7, 47]


def func4():
    return {'ieoso': 100, 'bmkgp': 82, 'pljzu': 68}


def func5():
    return 19.29


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
