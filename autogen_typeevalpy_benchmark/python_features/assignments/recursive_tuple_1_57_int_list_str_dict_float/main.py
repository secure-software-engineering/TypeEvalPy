# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 76


def func2():
    return [40, 94, 53]


def func3():
    return 'tywco'


def func4():
    return {'uvgft': 23, 'saemc': 48, 'ukkhl': 24}


def func5():
    return 70.7


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
