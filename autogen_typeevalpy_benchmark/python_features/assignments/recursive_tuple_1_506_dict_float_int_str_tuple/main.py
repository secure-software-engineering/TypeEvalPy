# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'qbjia': 13, 'kvtcz': 15, 'vneaw': 32}


def func2():
    return 45.52


def func3():
    return 8


def func4():
    return 'gbhpx'


def func5():
    return (17, 76, 69)


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
