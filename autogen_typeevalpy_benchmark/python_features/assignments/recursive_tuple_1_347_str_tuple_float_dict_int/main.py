# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'pyfgl'


def func2():
    return (10, 8, 61)


def func3():
    return 26.01


def func4():
    return {'ujrur': 82, 'otjxr': 24, 'aljwk': 39}


def func5():
    return 6


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
