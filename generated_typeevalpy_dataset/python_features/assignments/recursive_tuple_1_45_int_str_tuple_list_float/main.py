# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 70


def func2():
    return 'egbbk'


def func3():
    return (40, 27, 70)


def func4():
    return [39, 23, 48]


def func5():
    return 30.83


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