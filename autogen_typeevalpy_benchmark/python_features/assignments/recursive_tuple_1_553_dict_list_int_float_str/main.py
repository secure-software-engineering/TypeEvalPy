# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'srtwj': 59, 'iwtaa': 31, 'ojutz': 76}


def func2():
    return [15, 79, 1]


def func3():
    return 1


def func4():
    return 52.1


def func5():
    return 'ouzdd'


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
