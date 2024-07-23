# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 73


def func2():
    return [96, 23, 68]


def func3():
    return 'solia'


def func4():
    return (82, 46, 40)


def func5():
    return 84.85


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
