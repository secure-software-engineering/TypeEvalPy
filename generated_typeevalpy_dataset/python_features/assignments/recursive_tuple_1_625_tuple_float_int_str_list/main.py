# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (32, 67, 68)


def func2():
    return 59.23


def func3():
    return 52


def func4():
    return 'qwrab'


def func5():
    return [38, 55, 65]


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
