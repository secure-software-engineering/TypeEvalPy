# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 96.02


def func2():
    return 'cadau'


def func3():
    return 73


def func4():
    return [70, 10, 44]


def func5():
    return {'esxqm': 10, 'vomjq': 73, 'odblj': 11}


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
