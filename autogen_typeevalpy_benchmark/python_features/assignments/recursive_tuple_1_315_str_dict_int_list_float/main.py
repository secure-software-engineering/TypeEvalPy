# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'falqd'


def func2():
    return {'wutqh': 7, 'gaflm': 32, 'mmwmk': 19}


def func3():
    return 82


def func4():
    return [13, 38, 48]


def func5():
    return 6.26


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
