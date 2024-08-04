# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 51


def func2():
    return [91, 76, 11]


def func3():
    return 'nekvg'


def func4():
    return 30.92


def func5():
    return (69, 85, 49)


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
