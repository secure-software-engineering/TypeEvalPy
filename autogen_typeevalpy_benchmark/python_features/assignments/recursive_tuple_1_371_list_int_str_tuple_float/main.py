# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [62, 55, 13]


def func2():
    return 87


def func3():
    return 'vwtui'


def func4():
    return (44, 97, 16)


def func5():
    return 25.94


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
