# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'ylgch': 56, 'kobjm': 100, 'mbwhq': 3}


def func2():
    return 69


def func3():
    return 'zkeex'


def func4():
    return 66.02


def func5():
    return [37, 8, 92]


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
