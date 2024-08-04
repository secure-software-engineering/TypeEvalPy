# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (85, 27, 19)


def func2():
    return 'vulfd'


def func3():
    return 29


def func4():
    return 97.56


def func5():
    return [33, 49, 13]


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
