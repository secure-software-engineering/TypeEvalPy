# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [26, 60, 76]


def func2():
    return 'ldkpt'


def func3():
    return 11.1


def func4():
    return {'xydmy': 38, 'mogvt': 75, 'lfrnp': 73}


def func5():
    return 15


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
