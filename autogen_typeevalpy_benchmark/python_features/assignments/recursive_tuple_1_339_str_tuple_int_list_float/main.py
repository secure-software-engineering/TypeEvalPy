# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'qoziw'


def func2():
    return (94, 43, 96)


def func3():
    return 72


def func4():
    return [13, 13, 43]


def func5():
    return 90.69


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
