# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'tfjxt': 32, 'marmz': 12, 'rcpyp': 69}


def func2():
    return (82, 91, 92)


def func3():
    return 'qbgva'


def func4():
    return 29.58


def func5():
    return 63


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
