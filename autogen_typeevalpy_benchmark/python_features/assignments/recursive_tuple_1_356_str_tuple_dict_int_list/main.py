# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'tuubk'


def func2():
    return (73, 6, 43)


def func3():
    return {'rxpzt': 100, 'sfcie': 42, 'cjqhp': 87}


def func4():
    return 13


def func5():
    return [65, 73, 12]


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
