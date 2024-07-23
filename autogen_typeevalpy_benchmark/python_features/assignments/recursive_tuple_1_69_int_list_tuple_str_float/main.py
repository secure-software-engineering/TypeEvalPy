# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 63


def func2():
    return [52, 17, 73]


def func3():
    return (22, 4, 9)


def func4():
    return 'aijut'


def func5():
    return 15.51


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
