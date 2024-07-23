# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 23.8


def func2():
    return 'ixqnu'


def func3():
    return [4, 78, 48]


def func4():
    return (62, 4, 44)


def func5():
    return {'eobwb': 81, 'apbrv': 3, 'caegj': 97}


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
