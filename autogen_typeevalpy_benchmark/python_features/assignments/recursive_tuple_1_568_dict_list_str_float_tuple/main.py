# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'akqzz': 42, 'ciaea': 31, 'vkupk': 27}


def func2():
    return [86, 87, 92]


def func3():
    return 'uwpos'


def func4():
    return 55.14


def func5():
    return (25, 24, 24)


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
