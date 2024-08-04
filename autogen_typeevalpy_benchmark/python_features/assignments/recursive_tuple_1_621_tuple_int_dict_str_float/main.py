# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (17, 5, 76)


def func2():
    return 79


def func3():
    return {'oqvje': 30, 'uydxi': 4, 'zqbei': 73}


def func4():
    return 'yzlyc'


def func5():
    return 94.38


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
