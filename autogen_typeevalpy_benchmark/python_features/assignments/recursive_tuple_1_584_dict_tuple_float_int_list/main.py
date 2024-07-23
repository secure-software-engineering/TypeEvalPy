# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'pdtis': 49, 'vepyv': 84, 'fawzv': 82}


def func2():
    return (39, 11, 43)


def func3():
    return 97.64


def func4():
    return 57


def func5():
    return [41, 68, 86]


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
