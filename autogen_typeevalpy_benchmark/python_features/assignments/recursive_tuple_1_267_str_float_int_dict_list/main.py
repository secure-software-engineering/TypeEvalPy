# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'ieqsg'


def func2():
    return 99.62


def func3():
    return 44


def func4():
    return {'bttlc': 87, 'odzqt': 35, 'ajxja': 90}


def func5():
    return [49, 43, 47]


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
