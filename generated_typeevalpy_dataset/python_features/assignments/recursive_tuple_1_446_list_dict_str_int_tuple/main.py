# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [9, 8, 87]


def func2():
    return {'mxrni': 62, 'chrom': 83, 'ibjpb': 9}


def func3():
    return 'sinxv'


def func4():
    return 97


def func5():
    return (84, 31, 74)


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
