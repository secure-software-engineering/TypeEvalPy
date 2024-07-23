# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 34.9


def func2():
    return [26, 84, 14]


def func3():
    return 'uapjh'


def func4():
    return (27, 64, 86)


def func5():
    return 1


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
