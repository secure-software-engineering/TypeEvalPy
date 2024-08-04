# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'rtxdu'


def func2():
    return [38, 25, 88]


def func3():
    return {'rsofm': 48, 'ndshg': 32, 'pqixv': 51}


def func4():
    return 48.95


def func5():
    return (35, 73, 59)


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
