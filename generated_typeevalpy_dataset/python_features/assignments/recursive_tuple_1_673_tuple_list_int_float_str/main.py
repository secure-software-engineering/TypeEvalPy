# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (44, 80, 84)


def func2():
    return [86, 95, 46]


def func3():
    return 95


def func4():
    return 95.09


def func5():
    return 'btbkk'


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