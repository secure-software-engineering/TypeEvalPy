# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 75.42


def func2():
    return [10, 80, 51]


def func3():
    return 40


def func4():
    return 'amanl'


def func5():
    return {'vaoeg': 99, 'kegsj': 22, 'uwbdq': 82}


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
