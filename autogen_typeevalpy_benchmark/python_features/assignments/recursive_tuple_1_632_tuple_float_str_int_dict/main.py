# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (7, 44, 21)


def func2():
    return 80.23


def func3():
    return 'grcra'


def func4():
    return 59


def func5():
    return {'ureaf': 87, 'xrmyj': 87, 'hmsuw': 99}


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
