# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [65, 37, 66]


def func2():
    return {'xvieg': 28, 'xyglv': 58, 'fnjbp': 91}


def func3():
    return 71


def func4():
    return (14, 2, 83)


def func5():
    return 'rturg'


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
