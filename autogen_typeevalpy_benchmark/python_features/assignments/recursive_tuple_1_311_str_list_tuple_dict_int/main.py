# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'azwmh'


def func2():
    return [23, 93, 60]


def func3():
    return (40, 31, 29)


def func4():
    return {'vrlcp': 71, 'otrze': 19, 'qmrpt': 24}


def func5():
    return 62


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
