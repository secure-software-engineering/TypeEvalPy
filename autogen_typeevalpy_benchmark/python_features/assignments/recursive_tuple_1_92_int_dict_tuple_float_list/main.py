# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 92


def func2():
    return {'fcvlt': 6, 'ohgkb': 73, 'pabhr': 33}


def func3():
    return (2, 8, 79)


def func4():
    return 86.31


def func5():
    return [30, 6, 52]


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
