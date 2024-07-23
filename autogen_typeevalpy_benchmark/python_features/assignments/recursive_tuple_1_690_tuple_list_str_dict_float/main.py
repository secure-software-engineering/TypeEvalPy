# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (99, 43, 67)


def func2():
    return [65, 19, 52]


def func3():
    return 'jmtpj'


def func4():
    return {'nzwbv': 33, 'msgqi': 36, 'mrcdi': 6}


def func5():
    return 52.61


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
