# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [3, 17, 25]


def func2():
    return 'hsepr'


def func3():
    return 2


def func4():
    return {'pdnlw': 31, 'hqkal': 13, 'rchpi': 82}


def func5():
    return 77.58


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
