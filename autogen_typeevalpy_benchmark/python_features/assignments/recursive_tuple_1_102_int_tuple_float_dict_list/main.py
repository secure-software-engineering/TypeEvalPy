# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 14


def func2():
    return (98, 21, 24)


def func3():
    return 64.58


def func4():
    return {'dtgcp': 92, 'oipzz': 67, 'ujayk': 85}


def func5():
    return [49, 47, 70]


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
