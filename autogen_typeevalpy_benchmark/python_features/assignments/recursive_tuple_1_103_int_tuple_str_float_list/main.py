# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 13


def func2():
    return (59, 41, 22)


def func3():
    return 'yehjc'


def func4():
    return 18.74


def func5():
    return [99, 59, 34]


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
