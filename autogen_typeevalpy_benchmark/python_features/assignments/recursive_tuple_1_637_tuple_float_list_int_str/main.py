# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (2, 90, 35)


def func2():
    return 71.55


def func3():
    return [10, 96, 1]


def func4():
    return 91


def func5():
    return 'uipxa'


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
