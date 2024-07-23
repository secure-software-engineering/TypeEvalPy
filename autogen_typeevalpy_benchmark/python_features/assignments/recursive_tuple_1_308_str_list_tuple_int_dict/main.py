# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'dsbks'


def func2():
    return [66, 89, 75]


def func3():
    return (10, 70, 48)


def func4():
    return 58


def func5():
    return {'ylhel': 16, 'oypbe': 26, 'vfysv': 65}


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
