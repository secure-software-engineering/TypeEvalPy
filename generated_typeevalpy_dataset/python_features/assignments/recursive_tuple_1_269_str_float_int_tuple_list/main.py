# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'kxvcw'


def func2():
    return 88.01


def func3():
    return 71


def func4():
    return (59, 25, 9)


def func5():
    return [63, 80, 52]


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
