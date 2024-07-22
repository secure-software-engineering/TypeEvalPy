# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [1, 86, 55]


def func2():
    return 56


def func3():
    return 41.2


def func4():
    return 'edsdh'


def func5():
    return {'pvivi': 38, 'igirk': 15, 'tecty': 95}


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
