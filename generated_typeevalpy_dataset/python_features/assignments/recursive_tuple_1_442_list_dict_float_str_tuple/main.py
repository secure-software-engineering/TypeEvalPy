# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [31, 2, 69]


def func2():
    return {'lmsqj': 67, 'fmydq': 12, 'gmwwo': 22}


def func3():
    return 54.39


def func4():
    return 'brpgq'


def func5():
    return (89, 27, 32)


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
