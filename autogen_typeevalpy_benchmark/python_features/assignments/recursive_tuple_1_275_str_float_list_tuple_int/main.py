# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'jcvsa'


def func2():
    return 21.81


def func3():
    return [51, 21, 15]


def func4():
    return (47, 9, 88)


def func5():
    return 37


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
