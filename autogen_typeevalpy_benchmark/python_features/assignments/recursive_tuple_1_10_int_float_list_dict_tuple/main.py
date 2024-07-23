# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 86


def func2():
    return 26.16


def func3():
    return [61, 52, 73]


def func4():
    return {'kondm': 11, 'hgtsi': 22, 'vhoaw': 42}


def func5():
    return (18, 20, 25)


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
