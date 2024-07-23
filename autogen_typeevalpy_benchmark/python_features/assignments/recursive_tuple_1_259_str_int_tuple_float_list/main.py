# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'wokzm'


def func2():
    return 2


def func3():
    return (53, 52, 21)


def func4():
    return 66.79


def func5():
    return [10, 61, 49]


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
