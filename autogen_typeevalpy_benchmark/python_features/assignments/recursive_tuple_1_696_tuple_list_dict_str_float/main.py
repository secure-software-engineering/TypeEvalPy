# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (10, 56, 64)


def func2():
    return [77, 28, 5]


def func3():
    return {'bgoca': 20, 'hrpru': 68, 'bixex': 72}


def func4():
    return 'vkkdx'


def func5():
    return 99.93


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
