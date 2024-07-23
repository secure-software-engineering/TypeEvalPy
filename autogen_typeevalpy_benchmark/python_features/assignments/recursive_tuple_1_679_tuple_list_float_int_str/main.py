# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (61, 56, 10)


def func2():
    return [63, 42, 77]


def func3():
    return 67.74


def func4():
    return 100


def func5():
    return 'rhyde'


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
