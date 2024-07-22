# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 61.53


def func2():
    return [64, 24, 12]


def func3():
    return 'uxege'


def func4():
    return (44, 5, 11)


def func5():
    return 93


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
