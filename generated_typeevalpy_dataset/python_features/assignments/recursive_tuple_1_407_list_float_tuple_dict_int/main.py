# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [48, 50, 40]


def func2():
    return 39.9


def func3():
    return (58, 52, 13)


def func4():
    return {'hdhyw': 42, 'vpgpm': 26, 'koryz': 55}


def func5():
    return 45


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
