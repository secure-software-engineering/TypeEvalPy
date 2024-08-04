# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 1.56


def func2():
    return {'ybkqd': 72, 'lhvfr': 72, 'gvalj': 95}


def func3():
    return (26, 28, 80)


def func4():
    return [65, 57, 36]


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
