# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'vyhtf'


def func2():
    return [62, 12, 80]


def func3():
    return 79.98


def func4():
    return {'nylol': 1, 'migqt': 6, 'kqpfp': 37}


def func5():
    return (93, 36, 23)


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
