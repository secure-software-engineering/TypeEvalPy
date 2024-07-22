# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'rqcra'


def func2():
    return (7, 56, 2)


def func3():
    return 64


def func4():
    return {'jaoze': 64, 'bsugl': 17, 'owmux': 36}


def func5():
    return 21.04


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
