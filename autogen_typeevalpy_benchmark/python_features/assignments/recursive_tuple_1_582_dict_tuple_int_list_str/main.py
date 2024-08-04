# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'fotti': 90, 'bwqpz': 21, 'isfpd': 98}


def func2():
    return (64, 24, 70)


def func3():
    return 12


def func4():
    return [21, 74, 16]


def func5():
    return 'vfqhu'


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
