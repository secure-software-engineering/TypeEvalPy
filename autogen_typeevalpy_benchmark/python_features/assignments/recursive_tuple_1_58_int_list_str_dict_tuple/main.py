# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 26


def func2():
    return [63, 24, 65]


def func3():
    return 'ylveb'


def func4():
    return {'etgxk': 87, 'qqweh': 98, 'jhipm': 13}


def func5():
    return (2, 8, 35)


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
