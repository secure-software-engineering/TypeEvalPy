# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [83, 84, 53]


def func2():
    return (5, 33, 67)


def func3():
    return 53


def func4():
    return 49.27


def func5():
    return 'fhtdm'


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
