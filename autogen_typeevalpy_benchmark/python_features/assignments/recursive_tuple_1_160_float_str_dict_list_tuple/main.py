# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 10.47


def func2():
    return 'canoj'


def func3():
    return {'pyknw': 89, 'qqelk': 90, 'oribo': 38}


def func4():
    return [71, 34, 68]


def func5():
    return (88, 15, 63)


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
