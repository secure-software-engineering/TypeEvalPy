# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (68, 81, 16)


def func2():
    return [78, 44, 75]


def func3():
    return 72


def func4():
    return 'ohrka'


def func5():
    return {'pcawh': 70, 'oipsv': 76, 'wxkrr': 59}


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
