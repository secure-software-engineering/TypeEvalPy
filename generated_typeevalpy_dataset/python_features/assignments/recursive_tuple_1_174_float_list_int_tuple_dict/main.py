# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 70.28


def func2():
    return [23, 71, 90]


def func3():
    return 14


def func4():
    return (61, 17, 70)


def func5():
    return {'klrux': 59, 'mjcne': 35, 'xkwmc': 81}


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
