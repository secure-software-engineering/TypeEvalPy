# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [64, 31, 52]


def func2():
    return 67


def func3():
    return (100, 19, 2)


def func4():
    return 37.14


def func5():
    return 'aocve'


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