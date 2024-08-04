# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'cswkz': 36, 'fbscl': 5, 'vqxbc': 2}


def func2():
    return [27, 39, 61]


def func3():
    return 'vgtmc'


def func4():
    return 60


def func5():
    return (98, 84, 72)


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
