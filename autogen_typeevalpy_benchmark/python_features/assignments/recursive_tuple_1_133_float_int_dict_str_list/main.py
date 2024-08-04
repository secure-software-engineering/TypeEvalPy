# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 54.95


def func2():
    return 58


def func3():
    return {'zwexj': 73, 'ipyhe': 45, 'psvdu': 37}


def func4():
    return 'caydr'


def func5():
    return [67, 38, 80]


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
