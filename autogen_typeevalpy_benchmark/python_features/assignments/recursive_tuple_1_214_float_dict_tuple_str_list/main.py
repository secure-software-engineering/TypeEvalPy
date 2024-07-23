# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 21.23


def func2():
    return {'zchbw': 58, 'zaxow': 75, 'ncuhw': 5}


def func3():
    return (17, 73, 63)


def func4():
    return 'onafg'


def func5():
    return [37, 21, 98]


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
