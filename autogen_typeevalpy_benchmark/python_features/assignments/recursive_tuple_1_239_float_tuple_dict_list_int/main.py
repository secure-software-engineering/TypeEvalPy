# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 22.24


def func2():
    return (42, 95, 90)


def func3():
    return {'dxrgg': 7, 'wxupq': 60, 'ndpvz': 29}


def func4():
    return [2, 30, 40]


def func5():
    return 95


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
