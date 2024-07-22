# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [56, 59, 65]


def func2():
    return (66, 78, 14)


def func3():
    return 'dmygh'


def func4():
    return {'ewxob': 92, 'pyqgt': 87, 'hznpa': 16}


def func5():
    return 16


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
