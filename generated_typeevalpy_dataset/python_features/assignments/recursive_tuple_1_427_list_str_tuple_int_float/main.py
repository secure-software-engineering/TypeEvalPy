# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [84, 1, 42]


def func2():
    return 'cztni'


def func3():
    return (70, 64, 18)


def func4():
    return 48


def func5():
    return 67.59


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
