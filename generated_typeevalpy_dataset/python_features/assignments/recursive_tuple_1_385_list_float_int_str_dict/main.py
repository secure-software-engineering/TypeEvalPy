# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [44, 8, 38]


def func2():
    return 36.92


def func3():
    return 41


def func4():
    return 'pxtft'


def func5():
    return {'khchs': 92, 'xdveh': 30, 'rljux': 79}


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
