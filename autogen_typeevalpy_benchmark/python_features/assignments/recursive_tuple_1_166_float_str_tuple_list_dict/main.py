# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 54.25


def func2():
    return 'fmvjh'


def func3():
    return (74, 55, 94)


def func4():
    return [57, 67, 17]


def func5():
    return {'vhcsv': 94, 'llgwz': 10, 'tdjcu': 42}


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
