# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 87


def func2():
    return 41.01


def func3():
    return 'bbfym'


def func4():
    return [39, 75, 51]


def func5():
    return {'tdtoe': 19, 'hkjae': 37, 'oypsy': 76}


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
