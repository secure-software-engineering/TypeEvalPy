# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'crzrk': 7, 'niakl': 19, 'krzld': 48}


def func2():
    return 'zknhw'


def func3():
    return 32.02


def func4():
    return 40


def func5():
    return [46, 54, 84]


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
