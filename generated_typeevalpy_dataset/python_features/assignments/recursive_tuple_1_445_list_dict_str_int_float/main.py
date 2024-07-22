# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [70, 31, 98]


def func2():
    return {'etarg': 94, 'clavu': 26, 'mwmjr': 49}


def func3():
    return 'kiwis'


def func4():
    return 89


def func5():
    return 88.59


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
