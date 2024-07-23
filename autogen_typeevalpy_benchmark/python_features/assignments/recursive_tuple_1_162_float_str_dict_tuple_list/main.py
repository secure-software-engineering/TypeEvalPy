# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 9.3


def func2():
    return 'iyhot'


def func3():
    return {'ceylv': 54, 'dupwt': 52, 'wdrrx': 84}


def func4():
    return (9, 39, 66)


def func5():
    return [76, 40, 69]


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
