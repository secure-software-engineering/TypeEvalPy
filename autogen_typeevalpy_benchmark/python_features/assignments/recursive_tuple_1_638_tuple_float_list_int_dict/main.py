# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (28, 37, 37)


def func2():
    return 76.45


def func3():
    return [51, 52, 21]


def func4():
    return 22


def func5():
    return {'prdmm': 38, 'ikazk': 58, 'vvikl': 82}


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
