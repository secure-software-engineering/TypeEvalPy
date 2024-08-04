# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [12, 15, 15]


def func2():
    return 38.88


def func3():
    return (14, 17, 24)


def func4():
    return 'bqadi'


def func5():
    return 96


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
