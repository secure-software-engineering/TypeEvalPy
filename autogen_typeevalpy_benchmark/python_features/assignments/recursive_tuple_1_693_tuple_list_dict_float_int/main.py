# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (36, 74, 27)


def func2():
    return [16, 17, 16]


def func3():
    return {'zkftu': 52, 'leqvt': 27, 'zqksi': 25}


def func4():
    return 60.19


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
