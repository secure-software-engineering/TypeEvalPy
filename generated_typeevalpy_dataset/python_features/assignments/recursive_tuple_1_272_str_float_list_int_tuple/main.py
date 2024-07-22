# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'fcbwn'


def func2():
    return 40.4


def func3():
    return [42, 49, 91]


def func4():
    return 99


def func5():
    return (73, 22, 85)


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
