# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 66


def func2():
    return 86.46


def func3():
    return {'dfmty': 39, 'jypkd': 38, 'obdjz': 63}


def func4():
    return 'aduky'


def func5():
    return [40, 37, 28]


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
