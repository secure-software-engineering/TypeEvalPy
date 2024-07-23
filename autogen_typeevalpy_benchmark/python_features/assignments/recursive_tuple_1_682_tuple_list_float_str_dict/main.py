# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (93, 15, 39)


def func2():
    return [55, 33, 90]


def func3():
    return 33.28


def func4():
    return 'awsar'


def func5():
    return {'erbji': 37, 'hkqjw': 41, 'rirzz': 78}


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
