# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 57.36


def func2():
    return {'pwcxu': 66, 'fupla': 37, 'tpmen': 83}


def func3():
    return (39, 34, 69)


def func4():
    return 32


def func5():
    return [44, 36, 87]


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
