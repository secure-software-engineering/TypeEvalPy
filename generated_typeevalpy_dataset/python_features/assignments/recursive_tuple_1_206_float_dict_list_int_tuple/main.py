# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 85.09


def func2():
    return {'qzdia': 43, 'navhe': 85, 'ghhkr': 1}


def func3():
    return [27, 29, 70]


def func4():
    return 52


def func5():
    return (46, 69, 95)


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
