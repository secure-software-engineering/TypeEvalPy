# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [88, 61, 13]


def func2():
    return 34


def func3():
    return 16.05


def func4():
    return (82, 20, 79)


def func5():
    return 'jwlru'


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
