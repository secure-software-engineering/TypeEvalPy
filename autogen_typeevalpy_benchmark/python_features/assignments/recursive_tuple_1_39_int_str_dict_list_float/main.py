# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 2


def func2():
    return 'mrjfl'


def func3():
    return {'ttrhp': 49, 'oadzz': 27, 'ouxok': 51}


def func4():
    return [9, 69, 50]


def func5():
    return 19.65


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
