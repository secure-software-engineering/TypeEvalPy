# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [58, 33, 27]


def func2():
    return (94, 25, 79)


def func3():
    return {'amnxo': 30, 'orjzk': 19, 'vzzzz': 93}


def func4():
    return 53


def func5():
    return 53.88


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
