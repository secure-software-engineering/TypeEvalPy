# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [59, 40, 45]


def func2():
    return (70, 23, 92)


def func3():
    return 'yprco'


def func4():
    return {'azhvd': 29, 'adhpk': 67, 'fkzig': 84}


def func5():
    return 16.1


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
