# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 96


def func2():
    return (73, 8, 71)


def func3():
    return 24.91


def func4():
    return 'zzvxa'


def func5():
    return {'gehjd': 79, 'mfbgk': 18, 'udksb': 41}


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
