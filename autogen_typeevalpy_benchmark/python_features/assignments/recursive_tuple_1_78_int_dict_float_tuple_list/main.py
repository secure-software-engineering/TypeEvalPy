# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 24


def func2():
    return {'vagij': 73, 'zuzlz': 1, 'nhaqw': 22}


def func3():
    return 86.09


def func4():
    return (24, 36, 81)


def func5():
    return [94, 89, 24]


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
