# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'eiicd': 60, 'saeeq': 65, 'gbfir': 31}


def func2():
    return 71


def func3():
    return 81.05


def func4():
    return 'imaoo'


def func5():
    return [60, 57, 61]


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
