# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'tncir'


def func2():
    return 19


def func3():
    return {'oroht': 70, 'kukoi': 40, 'sclul': 81}


def func4():
    return (58, 62, 46)


def func5():
    return 98.59


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
