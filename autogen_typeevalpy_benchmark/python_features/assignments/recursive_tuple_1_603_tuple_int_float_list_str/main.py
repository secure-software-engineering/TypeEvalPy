# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (100, 11, 79)


def func2():
    return 3


def func3():
    return 77.34


def func4():
    return [58, 66, 83]


def func5():
    return 'ninip'


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
