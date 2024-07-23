# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 81


def func2():
    return [3, 16, 85]


def func3():
    return 72.53


def func4():
    return 'fbwdi'


def func5():
    return (89, 93, 77)


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
