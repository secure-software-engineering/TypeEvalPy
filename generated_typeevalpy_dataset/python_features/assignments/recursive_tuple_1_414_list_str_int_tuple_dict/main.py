# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [73, 19, 24]


def func2():
    return 'vrjuu'


def func3():
    return 60


def func4():
    return (68, 51, 27)


def func5():
    return {'pglgl': 51, 'guiky': 1, 'flzpa': 22}


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
