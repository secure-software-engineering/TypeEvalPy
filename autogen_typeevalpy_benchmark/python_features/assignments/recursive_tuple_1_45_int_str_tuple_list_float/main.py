# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 23


def func2():
    return 'hnkct'


def func3():
    return (87, 35, 20)


def func4():
    return [57, 46, 23]


def func5():
    return 22.45


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
