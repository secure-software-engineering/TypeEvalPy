# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [95, 2, 17]


def func2():
    return (5, 82, 27)


def func3():
    return 'zhsdw'


def func4():
    return 17


def func5():
    return 71.98


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
