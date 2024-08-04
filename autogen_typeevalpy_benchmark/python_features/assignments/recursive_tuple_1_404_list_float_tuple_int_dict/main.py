# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [1, 74, 54]


def func2():
    return 99.23


def func3():
    return (11, 27, 88)


def func4():
    return 76


def func5():
    return {'mpckq': 99, 'tdewy': 96, 'yktdc': 87}


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
