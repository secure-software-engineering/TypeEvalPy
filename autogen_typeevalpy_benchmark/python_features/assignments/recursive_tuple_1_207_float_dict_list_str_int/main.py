# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 69.86


def func2():
    return {'ppasy': 75, 'hgnvy': 39, 'mhdgs': 6}


def func3():
    return [16, 60, 93]


def func4():
    return 'cfaeu'


def func5():
    return 33


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
