# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 18


def func2():
    return 'jucyh'


def func3():
    return [31, 48, 48]


def func4():
    return {'ryzzw': 32, 'wbdyu': 6, 'ejjpz': 98}


def func5():
    return 61.99


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
