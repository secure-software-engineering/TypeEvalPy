# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (39, 99, 39)


def func2():
    return [79, 57, 55]


def func3():
    return 'ueplf'


def func4():
    return 18.21


def func5():
    return {'bvygt': 46, 'qmxvh': 52, 'oqjqv': 100}


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
