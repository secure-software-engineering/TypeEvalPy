# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 2


def func2():
    return [7, 21, 80]


def func3():
    return (37, 96, 35)


def func4():
    return {'jvetw': 34, 'wsnge': 87, 'cfiiw': 65}


def func5():
    return 78.25


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
