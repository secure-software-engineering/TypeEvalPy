# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'fntwc': 80, 'cgzmo': 85, 'hxoxa': 93}


def func2():
    return 'ovvlp'


def func3():
    return 37.67


def func4():
    return 19


def func5():
    return [72, 55, 55]


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
