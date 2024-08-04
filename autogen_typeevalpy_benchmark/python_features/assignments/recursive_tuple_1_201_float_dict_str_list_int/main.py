# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 35.29


def func2():
    return {'lmtfs': 48, 'rgawz': 39, 'qoifz': 38}


def func3():
    return 'tlmep'


def func4():
    return [80, 46, 73]


def func5():
    return 56


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
