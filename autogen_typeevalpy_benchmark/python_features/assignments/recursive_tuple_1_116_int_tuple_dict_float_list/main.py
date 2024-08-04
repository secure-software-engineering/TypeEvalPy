# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 15


def func2():
    return (59, 77, 16)


def func3():
    return {'chxcm': 41, 'jvkma': 82, 'bybrj': 58}


def func4():
    return 81.05


def func5():
    return [24, 39, 2]


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
