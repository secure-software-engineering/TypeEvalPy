# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 21.75


def func2():
    return (90, 87, 76)


def func3():
    return [74, 55, 88]


def func4():
    return 75


def func5():
    return 'xzypt'


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
