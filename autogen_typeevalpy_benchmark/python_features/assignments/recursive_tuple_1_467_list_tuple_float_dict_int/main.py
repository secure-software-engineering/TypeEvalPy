# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [97, 99, 44]


def func2():
    return (31, 62, 69)


def func3():
    return 76.79


def func4():
    return {'swbzp': 18, 'exmen': 22, 'iwwrz': 93}


def func5():
    return 97


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
