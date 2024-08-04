# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [1, 25, 40]


def func2():
    return 63.18


def func3():
    return 16


def func4():
    return {'wxvbv': 51, 'xpefv': 40, 'igucj': 12}


def func5():
    return (42, 38, 59)


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
