# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'cfuhs'


def func2():
    return 13.07


def func3():
    return {'xotwc': 16, 'nnbyz': 10, 'kbozo': 90}


def func4():
    return 79


def func5():
    return [48, 96, 10]


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
