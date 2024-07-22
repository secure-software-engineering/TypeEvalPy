# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [95, 69, 8]


def func2():
    return 89.22


def func3():
    return 'rzelz'


def func4():
    return (19, 42, 16)


def func5():
    return 7


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
