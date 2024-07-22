# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 34.09


def func2():
    return (48, 17, 41)


def func3():
    return 16


def func4():
    return [14, 6, 80]


def func5():
    return 'ugnxv'


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
