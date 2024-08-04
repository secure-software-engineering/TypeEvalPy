# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 36


def func2():
    return [29, 93, 33]


def func3():
    return {'ryrrx': 96, 'qmuif': 95, 'oybix': 93}


def func4():
    return 'jqowv'


def func5():
    return 23.13


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
