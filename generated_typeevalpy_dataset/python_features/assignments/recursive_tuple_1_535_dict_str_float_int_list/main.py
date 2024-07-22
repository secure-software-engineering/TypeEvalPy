# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'mykiv': 69, 'abeub': 66, 'ztshy': 79}


def func2():
    return 'dgfhb'


def func3():
    return 82.28


def func4():
    return 86


def func5():
    return [84, 40, 69]


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
