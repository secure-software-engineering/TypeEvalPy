# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [91, 70, 95]


def func2():
    return {'oqiqy': 49, 'jkqap': 49, 'ofzmp': 33}


def func3():
    return 62.89


def func4():
    return 83


def func5():
    return 'qdklt'


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
