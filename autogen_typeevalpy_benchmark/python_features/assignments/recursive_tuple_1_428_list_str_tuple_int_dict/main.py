# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [24, 85, 69]


def func2():
    return 'odgok'


def func3():
    return (14, 43, 19)


def func4():
    return 50


def func5():
    return {'zumos': 94, 'rirdm': 52, 'zzimc': 48}


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
