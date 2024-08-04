# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [97, 79, 74]


def func2():
    return 'nnzpx'


def func3():
    return 89.85


def func4():
    return (11, 57, 3)


def func5():
    return 94


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
