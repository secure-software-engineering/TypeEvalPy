# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 65.11


def func2():
    return (79, 48, 4)


def func3():
    return [78, 92, 13]


def func4():
    return 66


def func5():
    return {'ithmt': 18, 'svxfg': 98, 'wkazd': 44}


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
