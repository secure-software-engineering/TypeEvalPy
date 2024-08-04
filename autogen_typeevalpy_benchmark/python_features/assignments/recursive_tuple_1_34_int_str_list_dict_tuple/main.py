# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 25


def func2():
    return 'whdgq'


def func3():
    return [36, 17, 66]


def func4():
    return {'zxfcm': 89, 'rbntq': 62, 'nmmij': 92}


def func5():
    return (64, 61, 35)


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
