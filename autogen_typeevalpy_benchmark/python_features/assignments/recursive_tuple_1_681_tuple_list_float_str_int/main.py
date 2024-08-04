# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (94, 95, 90)


def func2():
    return [11, 48, 88]


def func3():
    return 48.74


def func4():
    return 'pfjcs'


def func5():
    return 76


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
