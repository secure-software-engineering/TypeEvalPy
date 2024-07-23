# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 15


def func2():
    return 'kknvd'


def func3():
    return [7, 66, 69]


def func4():
    return (16, 31, 40)


def func5():
    return 35.61


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
