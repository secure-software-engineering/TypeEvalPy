# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (77, 22, 86)


def func2():
    return 'tdwwi'


def func3():
    return 99


def func4():
    return [77, 26, 24]


def func5():
    return 34.77


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
