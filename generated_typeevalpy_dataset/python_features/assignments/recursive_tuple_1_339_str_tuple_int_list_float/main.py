# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'qhrcy'


def func2():
    return (27, 26, 17)


def func3():
    return 53


def func4():
    return [76, 14, 24]


def func5():
    return 27.33


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
