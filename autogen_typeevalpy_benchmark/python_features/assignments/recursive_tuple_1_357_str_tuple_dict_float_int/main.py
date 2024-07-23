# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'koxbl'


def func2():
    return (96, 2, 41)


def func3():
    return {'qauuz': 25, 'hwpsh': 59, 'kiugx': 50}


def func4():
    return 49.53


def func5():
    return 51


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
