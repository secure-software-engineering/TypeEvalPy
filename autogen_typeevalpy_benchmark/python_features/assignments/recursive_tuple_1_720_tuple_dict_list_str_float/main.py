# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (36, 74, 37)


def func2():
    return {'svakd': 54, 'akdoi': 99, 'nicvb': 17}


def func3():
    return [97, 58, 54]


def func4():
    return 'seyts'


def func5():
    return 61.78


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
