# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'djjzj': 6, 'smjkb': 12, 'zlcmc': 41}


def func2():
    return (37, 99, 93)


def func3():
    return 80.19


def func4():
    return 40


def func5():
    return 'rdssu'


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