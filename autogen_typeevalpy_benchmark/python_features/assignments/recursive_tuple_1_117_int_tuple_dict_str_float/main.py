# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 23


def func2():
    return (85, 73, 81)


def func3():
    return {'pazzm': 47, 'poety': 15, 'faand': 28}


def func4():
    return 'adcrd'


def func5():
    return 28.09


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
