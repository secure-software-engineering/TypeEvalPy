# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (87, 70, 77)


def func2():
    return [80, 42, 65]


def func3():
    return 'emspl'


def func4():
    return 41


def func5():
    return 91.94


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
