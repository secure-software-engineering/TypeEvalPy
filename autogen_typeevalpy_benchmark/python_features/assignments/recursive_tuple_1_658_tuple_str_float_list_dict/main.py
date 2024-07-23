# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (99, 74, 3)


def func2():
    return 'rcrgh'


def func3():
    return 21.08


def func4():
    return [75, 36, 74]


def func5():
    return {'jaghz': 97, 'gufke': 32, 'ahnwf': 20}


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
