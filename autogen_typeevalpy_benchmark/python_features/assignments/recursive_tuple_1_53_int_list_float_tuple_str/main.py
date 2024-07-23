# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 53


def func2():
    return [11, 35, 48]


def func3():
    return 66.42


def func4():
    return (12, 89, 45)


def func5():
    return 'xrxjt'


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
