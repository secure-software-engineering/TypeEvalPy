# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'ofgdj': 10, 'xjerx': 74, 'nelrv': 39}


def func2():
    return [74, 56, 62]


def func3():
    return 31


def func4():
    return 'iqgra'


def func5():
    return (68, 87, 36)


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
