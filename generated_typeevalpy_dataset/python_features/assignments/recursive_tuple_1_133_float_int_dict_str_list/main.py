# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 30.12


def func2():
    return 77


def func3():
    return {'seyna': 38, 'zxrei': 24, 'mrhhb': 30}


def func4():
    return 'itmty'


def func5():
    return [50, 88, 74]


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
