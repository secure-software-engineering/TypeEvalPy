# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [76, 48, 43]


def func2():
    return {'nhxbu': 57, 'ptcir': 13, 'sxcxf': 56}


def func3():
    return 35.43


def func4():
    return (31, 92, 35)


def func5():
    return 67


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
