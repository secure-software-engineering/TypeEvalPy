# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'ncoat'


def func2():
    return [39, 64, 46]


def func3():
    return 49.95


def func4():
    return (42, 87, 3)


def func5():
    return {'tqgha': 11, 'bosda': 64, 'xnyxs': 50}


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
