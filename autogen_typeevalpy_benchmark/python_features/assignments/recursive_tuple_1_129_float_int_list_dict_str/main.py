# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 11.03


def func2():
    return 94


def func3():
    return [89, 35, 64]


def func4():
    return {'fujhp': 24, 'tcnsm': 43, 'hxgib': 59}


def func5():
    return 'damie'


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
