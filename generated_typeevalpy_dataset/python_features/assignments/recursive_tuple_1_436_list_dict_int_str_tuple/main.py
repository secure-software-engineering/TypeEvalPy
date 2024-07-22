# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [5, 5, 47]


def func2():
    return {'cfdaj': 58, 'einrm': 11, 'derzb': 93}


def func3():
    return 87


def func4():
    return 'leuhn'


def func5():
    return (46, 17, 35)


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
