# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'oathm': 3, 'ammge': 86, 'xaogs': 75}


def func2():
    return 70.04


def func3():
    return 'igoum'


def func4():
    return 50


def func5():
    return [57, 49, 19]


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
