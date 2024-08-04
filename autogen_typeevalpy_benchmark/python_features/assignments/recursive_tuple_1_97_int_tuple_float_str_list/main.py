# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 83


def func2():
    return (89, 2, 37)


def func3():
    return 12.02


def func4():
    return 'bqpee'


def func5():
    return [51, 55, 88]


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
