# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 8


def func2():
    return {'wydcf': 31, 'uijrv': 86, 'wgnzm': 54}


def func3():
    return [77, 58, 51]


def func4():
    return 'xsmzo'


def func5():
    return 52.19


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
