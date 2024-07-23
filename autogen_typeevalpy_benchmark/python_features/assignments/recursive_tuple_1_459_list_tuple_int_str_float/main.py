# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [9, 48, 95]


def func2():
    return (48, 98, 80)


def func3():
    return 92


def func4():
    return 'vwehy'


def func5():
    return 90.07


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
