# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (80, 65, 75)


def func2():
    return 'ademv'


def func3():
    return [8, 5, 91]


def func4():
    return 81.44


def func5():
    return {'tlvws': 54, 'qlrov': 64, 'zpsbu': 41}


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
