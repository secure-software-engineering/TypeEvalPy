# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (54, 20, 79)


def func2():
    return {'acyjw': 40, 'sdrnx': 71, 'zabqy': 73}


def func3():
    return 'lvtfv'


def func4():
    return [9, 47, 97]


def func5():
    return 56.23


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
