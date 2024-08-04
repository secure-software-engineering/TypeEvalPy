# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [54, 68, 8]


def func2():
    return {'khobl': 30, 'fozzx': 49, 'ynozi': 81}


def func3():
    return (39, 52, 18)


def func4():
    return 54.48


def func5():
    return 43


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
