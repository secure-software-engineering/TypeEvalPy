# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [45, 72, 74]


def func2():
    return 'bqqet'


def func3():
    return 41.37


def func4():
    return 22


def func5():
    return (44, 56, 46)


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
