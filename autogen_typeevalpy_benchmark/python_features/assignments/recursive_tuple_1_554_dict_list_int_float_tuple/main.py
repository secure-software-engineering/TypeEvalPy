# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'uaywj': 94, 'tqvdm': 59, 'ytpnu': 95}


def func2():
    return [92, 80, 6]


def func3():
    return 50


def func4():
    return 1.88


def func5():
    return (94, 44, 39)


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
