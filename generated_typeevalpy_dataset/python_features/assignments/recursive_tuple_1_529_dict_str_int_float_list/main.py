# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'kbpfy': 97, 'umzjx': 100, 'ehdrx': 78}


def func2():
    return 'mdmjc'


def func3():
    return 71


def func4():
    return 59.21


def func5():
    return [52, 72, 8]


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
