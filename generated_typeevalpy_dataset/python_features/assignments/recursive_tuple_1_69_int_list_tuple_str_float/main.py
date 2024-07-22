# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 22


def func2():
    return [18, 64, 91]


def func3():
    return (14, 77, 9)


def func4():
    return 'pnscp'


def func5():
    return 23.38


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
