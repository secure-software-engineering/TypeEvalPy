# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 41.25


def func2():
    return [1, 35, 89]


def func3():
    return 'fommy'


def func4():
    return {'glmot': 15, 'txlcd': 5, 'andfw': 55}


def func5():
    return 64


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
