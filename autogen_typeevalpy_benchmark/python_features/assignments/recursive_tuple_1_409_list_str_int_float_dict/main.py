# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [83, 22, 41]


def func2():
    return 'peppy'


def func3():
    return 68


def func4():
    return 82.5


def func5():
    return {'ouirz': 78, 'sjzon': 80, 'masxu': 33}


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
