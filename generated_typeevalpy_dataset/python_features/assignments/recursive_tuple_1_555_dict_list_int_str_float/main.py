# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'yqwrz': 93, 'zeunp': 90, 'ohaxg': 22}


def func2():
    return [67, 48, 18]


def func3():
    return 95


def func4():
    return 'trcbu'


def func5():
    return 35.3


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
