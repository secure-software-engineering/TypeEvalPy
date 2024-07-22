# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 51.2


def func2():
    return 70


def func3():
    return 'izadg'


def func4():
    return [20, 16, 93]


def func5():
    return (21, 19, 39)


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
