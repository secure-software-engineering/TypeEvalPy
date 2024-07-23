# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'fhnba': 52, 'jucso': 24, 'kjdln': 57}


def func2():
    return [95, 57, 61]


def func3():
    return 37.58


def func4():
    return 15


def func5():
    return 'ezovf'


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
