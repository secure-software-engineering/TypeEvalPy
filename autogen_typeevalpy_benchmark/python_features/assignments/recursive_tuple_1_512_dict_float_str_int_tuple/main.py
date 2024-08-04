# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'kztvr': 95, 'bkony': 50, 'lngii': 82}


def func2():
    return 40.77


def func3():
    return 'ykitp'


def func4():
    return 93


def func5():
    return (17, 28, 38)


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
