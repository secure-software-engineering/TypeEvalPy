# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 8


def func2():
    return 'kkqap'


def func3():
    return 20.64


def func4():
    return (41, 69, 71)


def func5():
    return [33, 23, 49]


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
