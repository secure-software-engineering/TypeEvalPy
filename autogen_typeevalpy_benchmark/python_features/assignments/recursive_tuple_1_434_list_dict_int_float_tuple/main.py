# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [71, 61, 6]


def func2():
    return {'jwhbi': 74, 'sgfht': 82, 'bheyh': 51}


def func3():
    return 24


def func4():
    return 65.59


def func5():
    return (39, 4, 43)


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
