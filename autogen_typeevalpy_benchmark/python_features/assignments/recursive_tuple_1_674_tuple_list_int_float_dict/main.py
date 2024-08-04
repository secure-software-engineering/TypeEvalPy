# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (44, 2, 21)


def func2():
    return [22, 10, 66]


def func3():
    return 86


def func4():
    return 10.31


def func5():
    return {'obvhz': 58, 'ftvrk': 37, 'xsgos': 4}


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
