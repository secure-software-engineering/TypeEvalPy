# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 6


def func2():
    return {'sgktd': 18, 'chvuv': 70, 'wbwza': 40}


def func3():
    return 'rmqog'


def func4():
    return (12, 74, 63)


def func5():
    return 61.8


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
