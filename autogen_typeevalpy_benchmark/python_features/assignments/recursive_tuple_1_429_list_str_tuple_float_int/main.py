# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [15, 6, 65]


def func2():
    return 'plwsi'


def func3():
    return (70, 69, 23)


def func4():
    return 96.82


def func5():
    return 81


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
