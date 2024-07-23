# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (17, 79, 38)


def func2():
    return [74, 16, 55]


def func3():
    return {'daqci': 33, 'ibcca': 61, 'gyoft': 82}


def func4():
    return 47


def func5():
    return 'phzwb'


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
