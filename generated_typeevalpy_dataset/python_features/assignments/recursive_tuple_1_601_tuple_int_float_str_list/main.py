# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (77, 10, 36)


def func2():
    return 87


def func3():
    return 20.67


def func4():
    return 'haszo'


def func5():
    return [7, 84, 59]


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
