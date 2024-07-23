# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'wgqhu': 97, 'ifkco': 63, 'wefni': 65}


def func2():
    return 'ezbus'


def func3():
    return [9, 63, 22]


def func4():
    return 24.41


def func5():
    return 55


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
