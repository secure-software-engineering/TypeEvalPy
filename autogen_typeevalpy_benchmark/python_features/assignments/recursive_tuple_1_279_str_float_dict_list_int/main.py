# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'nngjs'


def func2():
    return 85.42


def func3():
    return {'hfhaq': 59, 'kjuzl': 36, 'jeliy': 26}


def func4():
    return [91, 78, 59]


def func5():
    return 37


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
