# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 51.05


def func2():
    return 40


def func3():
    return {'jspej': 22, 'gfqzi': 34, 'opzap': 99}


def func4():
    return 'ovbdy'


def func5():
    return [82, 12, 13]


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
