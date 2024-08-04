# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 51.88


def func2():
    return 41


def func3():
    return 'tilen'


def func4():
    return (17, 29, 47)


def func5():
    return {'klqfk': 59, 'blryp': 24, 'clcca': 35}


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
