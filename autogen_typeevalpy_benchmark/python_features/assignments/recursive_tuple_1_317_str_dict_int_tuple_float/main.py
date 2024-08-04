# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'jijup'


def func2():
    return {'wtlnr': 19, 'otnzd': 19, 'vistq': 98}


def func3():
    return 26


def func4():
    return (12, 79, 50)


def func5():
    return 28.3


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
