# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'ytjvv'


def func2():
    return (13, 1, 25)


def func3():
    return {'fvjdc': 6, 'uruix': 86, 'gxbki': 25}


def func4():
    return [94, 75, 15]


def func5():
    return 55.19


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
