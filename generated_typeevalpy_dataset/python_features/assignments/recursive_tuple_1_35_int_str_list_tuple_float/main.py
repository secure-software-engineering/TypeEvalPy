# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 41


def func2():
    return 'ngdjf'


def func3():
    return [5, 29, 39]


def func4():
    return (41, 21, 81)


def func5():
    return 77.93


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
