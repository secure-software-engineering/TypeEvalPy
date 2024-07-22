# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [43, 31, 34]


def func2():
    return 13.05


def func3():
    return 'xlvkg'


def func4():
    return {'omins': 41, 'edaib': 91, 'qpgqj': 20}


def func5():
    return (65, 94, 93)


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
