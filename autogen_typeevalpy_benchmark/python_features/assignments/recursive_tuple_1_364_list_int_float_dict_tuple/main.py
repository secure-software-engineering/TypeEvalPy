# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [13, 23, 99]


def func2():
    return 28


def func3():
    return 26.15


def func4():
    return {'iblol': 6, 'cqmtq': 15, 'dfngt': 31}


def func5():
    return (39, 71, 1)


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
