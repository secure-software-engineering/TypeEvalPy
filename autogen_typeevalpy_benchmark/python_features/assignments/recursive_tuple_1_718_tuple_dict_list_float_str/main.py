# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (19, 34, 56)


def func2():
    return {'irnjp': 44, 'dmzsc': 27, 'rfrko': 68}


def func3():
    return [18, 6, 13]


def func4():
    return 10.74


def func5():
    return 'hwvue'


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
