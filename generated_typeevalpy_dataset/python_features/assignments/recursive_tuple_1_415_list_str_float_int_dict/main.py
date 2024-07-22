# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [94, 31, 76]


def func2():
    return 'txmpq'


def func3():
    return 93.11


def func4():
    return 31


def func5():
    return {'tigmj': 94, 'nkhxm': 65, 'tinmc': 33}


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
