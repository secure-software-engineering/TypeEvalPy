# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 42.32


def func2():
    return {'jlexm': 3, 'obrvy': 61, 'btjzh': 77}


def func3():
    return 23


def func4():
    return 'efgrp'


def func5():
    return (75, 88, 96)


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
