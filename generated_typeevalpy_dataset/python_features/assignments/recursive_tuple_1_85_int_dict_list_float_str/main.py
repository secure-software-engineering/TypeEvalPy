# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 99


def func2():
    return {'exumh': 43, 'bpexj': 6, 'fjhjf': 3}


def func3():
    return [36, 83, 75]


def func4():
    return 98.1


def func5():
    return 'jqzvu'


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
