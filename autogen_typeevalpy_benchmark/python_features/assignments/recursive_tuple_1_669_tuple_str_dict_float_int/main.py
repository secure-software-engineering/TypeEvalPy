# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (21, 25, 36)


def func2():
    return 'bfvky'


def func3():
    return {'afcww': 64, 'vdggk': 26, 'jkvbz': 24}


def func4():
    return 49.89


def func5():
    return 93


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
