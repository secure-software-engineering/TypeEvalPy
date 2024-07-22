# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (72, 62, 73)


def func2():
    return 20


def func3():
    return [11, 96, 84]


def func4():
    return 'thwzo'


def func5():
    return 20.05


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
