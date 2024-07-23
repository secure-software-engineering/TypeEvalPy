# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'kwfvw'


def func2():
    return (47, 13, 16)


def func3():
    return 13.31


def func4():
    return [13, 40, 61]


def func5():
    return {'bsgbk': 70, 'otwso': 78, 'bdwvx': 43}


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
