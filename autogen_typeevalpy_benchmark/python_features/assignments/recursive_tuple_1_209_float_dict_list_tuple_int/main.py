# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 97.64


def func2():
    return {'avbee': 5, 'idvdd': 63, 'giilc': 8}


def func3():
    return [41, 84, 33]


def func4():
    return (30, 60, 92)


def func5():
    return 5


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
