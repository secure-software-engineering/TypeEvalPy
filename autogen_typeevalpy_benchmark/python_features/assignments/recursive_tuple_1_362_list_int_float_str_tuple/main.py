# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [10, 12, 33]


def func2():
    return 5


def func3():
    return 69.85


def func4():
    return 'whnkt'


def func5():
    return (47, 81, 3)


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
