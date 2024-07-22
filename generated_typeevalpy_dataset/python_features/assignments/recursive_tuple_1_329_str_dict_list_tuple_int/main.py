# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'ngnii'


def func2():
    return {'duoja': 31, 'aqywp': 60, 'zidvd': 87}


def func3():
    return [35, 38, 63]


def func4():
    return (65, 90, 73)


def func5():
    return 14


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
