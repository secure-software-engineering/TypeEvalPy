# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'crpmy': 78, 'skcbo': 57, 'msosp': 53}


def func2():
    return 74.27


def func3():
    return [4, 27, 76]


def func4():
    return 6


def func5():
    return 'dkcgf'


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
