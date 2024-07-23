# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (1, 76, 77)


def func2():
    return [13, 4, 59]


def func3():
    return 4.39


def func4():
    return {'wevsa': 66, 'uwxjs': 80, 'lrpoo': 72}


def func5():
    return 'xogfp'


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
