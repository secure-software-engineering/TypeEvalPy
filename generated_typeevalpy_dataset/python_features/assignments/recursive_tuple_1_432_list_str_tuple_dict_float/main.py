# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [35, 68, 16]


def func2():
    return 'mxikc'


def func3():
    return (44, 75, 57)


def func4():
    return {'npdju': 8, 'rfmkx': 89, 'vmppo': 39}


def func5():
    return 24.23


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
