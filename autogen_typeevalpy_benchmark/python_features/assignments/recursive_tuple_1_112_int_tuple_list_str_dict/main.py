# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 12


def func2():
    return (14, 12, 84)


def func3():
    return [3, 79, 53]


def func4():
    return 'ctqoq'


def func5():
    return {'nurwf': 95, 'uocwy': 51, 'jumxq': 1}


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
