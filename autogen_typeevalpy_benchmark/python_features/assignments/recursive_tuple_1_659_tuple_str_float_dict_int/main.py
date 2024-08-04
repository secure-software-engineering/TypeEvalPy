# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (71, 6, 18)


def func2():
    return 'rleqh'


def func3():
    return 65.42


def func4():
    return {'vbgcx': 96, 'ptihv': 57, 'aeibc': 86}


def func5():
    return 59


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
