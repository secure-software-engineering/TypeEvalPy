# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [79, 79, 23]


def func2():
    return (70, 46, 45)


def func3():
    return 98


def func4():
    return 'txrib'


def func5():
    return 39.4


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
