# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (1, 28, 8)


def func2():
    return 'iuoik'


def func3():
    return 6.83


def func4():
    return {'iiddk': 9, 'bhzkk': 41, 'snptw': 35}


def func5():
    return [36, 73, 35]


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
