# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [73, 69, 53]


def func2():
    return {'cqxio': 98, 'puhlc': 50, 'rapny': 22}


def func3():
    return 17.44


def func4():
    return (93, 59, 29)


def func5():
    return 'smrac'


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
