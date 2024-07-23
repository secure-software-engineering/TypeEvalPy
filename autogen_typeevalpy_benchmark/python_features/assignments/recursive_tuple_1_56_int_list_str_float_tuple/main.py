# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 30


def func2():
    return [51, 74, 29]


def func3():
    return 'mavri'


def func4():
    return 38.61


def func5():
    return (11, 29, 2)


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
