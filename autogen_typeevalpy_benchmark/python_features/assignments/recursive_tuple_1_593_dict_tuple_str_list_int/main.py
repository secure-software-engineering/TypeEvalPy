# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'ulrdq': 62, 'nftvq': 84, 'tgbpj': 4}


def func2():
    return (61, 61, 86)


def func3():
    return 'znnmk'


def func4():
    return [94, 16, 33]


def func5():
    return 72


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
