# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (59, 68, 67)


def func2():
    return [60, 76, 41]


def func3():
    return 22.15


def func4():
    return 'drhph'


def func5():
    return {'lqlnb': 9, 'njbcs': 33, 'mgipi': 30}


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
