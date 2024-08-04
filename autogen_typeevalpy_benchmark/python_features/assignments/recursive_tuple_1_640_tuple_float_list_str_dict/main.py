# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (26, 88, 1)


def func2():
    return 7.72


def func3():
    return [30, 87, 93]


def func4():
    return 'qcmcl'


def func5():
    return {'jlbdg': 41, 'bgilg': 89, 'sztjc': 60}


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
