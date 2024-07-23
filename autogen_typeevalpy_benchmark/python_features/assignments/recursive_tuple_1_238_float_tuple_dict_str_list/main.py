# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 78.27


def func2():
    return (93, 44, 53)


def func3():
    return {'lfvju': 68, 'nuxga': 95, 'mmnlk': 58}


def func4():
    return 'zbblt'


def func5():
    return [60, 23, 92]


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
