# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [6, 72, 76]


def func2():
    return 69


def func3():
    return (99, 88, 35)


def func4():
    return 'gqouw'


def func5():
    return 95.36


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
