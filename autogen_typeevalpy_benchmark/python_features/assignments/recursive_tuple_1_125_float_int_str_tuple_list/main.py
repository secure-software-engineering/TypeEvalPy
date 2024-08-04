# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 8.44


def func2():
    return 64


def func3():
    return 'bafve'


def func4():
    return (14, 44, 27)


def func5():
    return [76, 98, 68]


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
