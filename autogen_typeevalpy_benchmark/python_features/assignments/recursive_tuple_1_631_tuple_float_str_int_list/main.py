# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (29, 11, 12)


def func2():
    return 20.77


def func3():
    return 'wdkci'


def func4():
    return 36


def func5():
    return [71, 44, 72]


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
