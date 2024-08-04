# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 34.64


def func2():
    return [6, 40, 58]


def func3():
    return 53


def func4():
    return {'fwnuc': 99, 'zpdoy': 71, 'ajuij': 9}


def func5():
    return 'rnjfe'


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
