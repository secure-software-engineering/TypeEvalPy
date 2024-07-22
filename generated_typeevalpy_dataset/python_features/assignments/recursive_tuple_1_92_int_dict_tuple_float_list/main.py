# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 13


def func2():
    return {'nwilx': 4, 'gahgd': 2, 'qklbx': 89}


def func3():
    return (53, 86, 98)


def func4():
    return 69.45


def func5():
    return [10, 64, 35]


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
