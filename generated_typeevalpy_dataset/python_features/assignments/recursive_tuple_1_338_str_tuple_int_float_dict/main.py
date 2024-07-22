# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'yrjff'


def func2():
    return (13, 19, 5)


def func3():
    return 6


def func4():
    return 14.93


def func5():
    return {'ljgvo': 85, 'ygrtf': 76, 'zezgv': 12}


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
