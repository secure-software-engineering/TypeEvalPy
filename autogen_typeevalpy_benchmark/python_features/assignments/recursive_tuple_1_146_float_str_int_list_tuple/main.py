# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 94.63


def func2():
    return 'geurp'


def func3():
    return 1


def func4():
    return [48, 46, 70]


def func5():
    return (52, 8, 60)


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
