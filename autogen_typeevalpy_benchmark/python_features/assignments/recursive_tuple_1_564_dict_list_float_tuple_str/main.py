# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'akruq': 55, 'cdrpu': 30, 'ocdgw': 40}


def func2():
    return [29, 44, 87]


def func3():
    return 59.09


def func4():
    return (37, 65, 65)


def func5():
    return 'usnhu'


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
