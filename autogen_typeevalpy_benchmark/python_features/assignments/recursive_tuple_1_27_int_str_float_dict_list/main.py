# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 3


def func2():
    return 'xbnoy'


def func3():
    return 13.67


def func4():
    return {'rlfkk': 74, 'eooeo': 33, 'djoez': 29}


def func5():
    return [52, 56, 38]


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
