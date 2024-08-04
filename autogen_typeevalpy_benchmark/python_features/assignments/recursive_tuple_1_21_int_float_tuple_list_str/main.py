# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 43


def func2():
    return 2.57


def func3():
    return (89, 18, 83)


def func4():
    return [1, 78, 61]


def func5():
    return 'aaeos'


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
