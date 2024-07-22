# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'pdpsz'


def func2():
    return 73.26


def func3():
    return 15


def func4():
    return {'jogwc': 18, 'qwtjo': 54, 'tulwt': 88}


def func5():
    return [42, 60, 87]


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
