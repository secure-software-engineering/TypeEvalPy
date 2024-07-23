# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (13, 88, 41)


def func2():
    return {'slbjz': 8, 'coozh': 40, 'kfnei': 89}


def func3():
    return 65


def func4():
    return 'yltzf'


def func5():
    return 48.02


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
