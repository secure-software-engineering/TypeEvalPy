# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 18


def func2():
    return 96.9


def func3():
    return [63, 40, 19]


def func4():
    return {'fhdhl': 97, 'nswvc': 90, 'wskum': 40}


def func5():
    return 'javsk'


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
