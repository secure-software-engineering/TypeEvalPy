# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'yfjzy': 37, 'qtxew': 70, 'ssqwp': 38}


def func2():
    return [65, 9, 29]


def func3():
    return (4, 2, 39)


def func4():
    return 14


def func5():
    return 74.12


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
