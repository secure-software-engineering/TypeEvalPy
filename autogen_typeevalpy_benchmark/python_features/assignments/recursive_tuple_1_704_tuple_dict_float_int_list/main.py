# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (38, 35, 15)


def func2():
    return {'zelab': 18, 'eaodp': 79, 'laiev': 86}


def func3():
    return 75.52


def func4():
    return 28


def func5():
    return [79, 25, 76]


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
