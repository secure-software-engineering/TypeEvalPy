# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 77.63


def func2():
    return [74, 52, 76]


def func3():
    return (4, 21, 66)


def func4():
    return {'ehpsn': 51, 'yodru': 22, 'bcudi': 59}


def func5():
    return 'adwhc'


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
