# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 70


def func2():
    return (93, 33, 82)


def func3():
    return 'auhyv'


def func4():
    return 88.46


def func5():
    return [100, 59, 23]


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
