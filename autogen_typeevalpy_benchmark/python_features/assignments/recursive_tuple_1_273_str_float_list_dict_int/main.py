# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'jnzic'


def func2():
    return 12.14


def func3():
    return [3, 86, 8]


def func4():
    return {'qmuaq': 17, 'inxvg': 65, 'ozvus': 93}


def func5():
    return 91


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
