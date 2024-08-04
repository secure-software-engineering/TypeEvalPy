# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 27.12


def func2():
    return 10


def func3():
    return [22, 87, 98]


def func4():
    return {'wpzpm': 39, 'gcvoz': 95, 'vnedc': 43}


def func5():
    return (58, 63, 95)


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
