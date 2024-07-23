# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 10.3


def func2():
    return [3, 14, 92]


def func3():
    return {'qrjzr': 6, 'nnwyx': 43, 'jvnpy': 13}


def func4():
    return 34


def func5():
    return (100, 39, 44)


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
