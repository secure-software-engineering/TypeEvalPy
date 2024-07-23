# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [28, 87, 20]


def func2():
    return 90.8


def func3():
    return 'vovwe'


def func4():
    return 58


def func5():
    return (98, 1, 2)


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
