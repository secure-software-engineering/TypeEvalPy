# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'xnvnt'


def func2():
    return [4, 89, 26]


def func3():
    return 87.6


def func4():
    return 34


def func5():
    return (18, 66, 14)


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
