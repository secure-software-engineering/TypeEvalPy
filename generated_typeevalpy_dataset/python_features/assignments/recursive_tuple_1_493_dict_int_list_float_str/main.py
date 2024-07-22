# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'tjczu': 51, 'mulln': 31, 'ovajk': 11}


def func2():
    return 51


def func3():
    return [50, 46, 51]


def func4():
    return 52.25


def func5():
    return 'tldov'


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
