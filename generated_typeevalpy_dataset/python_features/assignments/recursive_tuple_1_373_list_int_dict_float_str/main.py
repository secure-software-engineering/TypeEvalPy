# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [55, 83, 55]


def func2():
    return 31


def func3():
    return {'ynuxr': 55, 'ayypy': 18, 'iltum': 60}


def func4():
    return 14.2


def func5():
    return 'mshtv'


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