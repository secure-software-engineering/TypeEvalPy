# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 15


def func2():
    return {'ajtrs': 25, 'oboqb': 70, 'omnab': 66}


def func3():
    return 'trgdj'


def func4():
    return [100, 15, 42]


def func5():
    return 82.14


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
