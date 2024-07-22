# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (92, 12, 100)


def func2():
    return 85.07


def func3():
    return 7


def func4():
    return 'ucknw'


def func5():
    return {'jlxhb': 92, 'umbmv': 57, 'skvyj': 97}


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
