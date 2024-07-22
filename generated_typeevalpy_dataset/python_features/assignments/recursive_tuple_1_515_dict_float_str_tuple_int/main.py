# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'ezgcm': 15, 'kjlyt': 96, 'blkzw': 61}


def func2():
    return 11.0


def func3():
    return 'gkykq'


def func4():
    return (82, 19, 62)


def func5():
    return 25


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
