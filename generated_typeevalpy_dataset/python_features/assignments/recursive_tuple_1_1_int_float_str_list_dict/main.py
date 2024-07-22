# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 52


def func2():
    return 14.46


def func3():
    return 'jiipx'


def func4():
    return [56, 25, 64]


def func5():
    return {'exkqj': 68, 'ewthe': 14, 'vuamw': 65}


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
