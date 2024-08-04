# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'wfkzb'


def func2():
    return (88, 71, 57)


def func3():
    return 72.12


def func4():
    return 29


def func5():
    return {'tfcgx': 77, 'kzqxx': 69, 'cypcg': 96}


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
